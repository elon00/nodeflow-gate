"""Fail-closed source integrity checks; no simulated remote services."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SourceIntegrity(unittest.TestCase):
    def test_rust_source_has_no_embedded_control_bytes(self):
        source = (ROOT / "src" / "main.rs").read_bytes()
        disallowed = [b for b in source if b < 32 and b not in (9, 10, 13)]
        self.assertEqual(disallowed, [])

    def test_no_external_network_or_cryptography_claims_in_binary_source(self):
        source = (ROOT / "src" / "main.rs").read_text(encoding="utf-8")
        self.assertNotIn("Treasury Escrows Verified", source)
        self.assertNotIn("Security Vault: ACTIVE", source)
        self.assertNotIn("RPC Gateway: CONNECTED", source)


if __name__ == "__main__":
    unittest.main()
