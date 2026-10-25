"""Executable regression tests for the actual local Rust diagnostic.

These tests do NOT assert validator, RPC, PQC, TLS, or deployment readiness.
"""
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
MASK = (1 << 64) - 1
SEED = 0x55AA55AA55AA55AA
MIX = 0x9E3779B97F4A7C15


def reference_state(rounds=10_000):
    state = SEED
    for _ in range(rounds):
        rotated = ((state >> 7) | ((state << 57) & MASK)) & MASK
        state = (state ^ rotated ^ MIX) & MASK
    return state


class RustDiagnosticRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proc = subprocess.run(
            ["cargo", "run", "--quiet"],
            cwd=ROOT, text=True, capture_output=True, timeout=120, check=True,
        )

    def test_actual_binary_matches_independent_reference(self):
        match = re.search(r"^STATE_HEX=([0-9a-f]{16})$", self.proc.stdout, re.M)
        self.assertIsNotNone(match, self.proc.stdout)
        self.assertEqual(int(match.group(1), 16), reference_state())

    def test_binary_explicitly_disclaims_unimplemented_capabilities(self):
        out = self.proc.stdout
        self.assertIn("IMPLEMENTATION_STATUS=PLACEHOLDER", out)
        self.assertIn("SECURITY_STATUS=UNVERIFIED", out)
        self.assertIn("NETWORK_STATUS=NOT_CONNECTED", out)
        for forbidden in ("100/100", "FIPS", "CERTIFIED", "RPC Gateway: CONNECTED"):
            self.assertNotIn(forbidden, out)


if __name__ == "__main__":
    unittest.main()
