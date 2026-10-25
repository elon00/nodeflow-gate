# Nodeflow Gate — Local Diagnostic (NOT production ready)

**Status:** Placeholder Rust executable with a deterministic local state diagnostic. No validator orchestration, remote RPC, cryptographic verification, escrow, governance, x402 settlement, or deployment functionality has been independently implemented or accepted here.

The previous "100/100", FIPS, connected-RPC and production claims were unsupported and have been withdrawn. The integer mixing function is **not cryptography** and is not a Conway automaton.

## Reproduce the limited tests

```bash
cargo test --all-targets
python -m compileall -q tests
python -m unittest discover -s tests -p 'reality_*.py' -v
```

The Python regression suite runs the **actual local Rust binary** and compares its output against an independent reference calculation. A green workflow would prove only those narrow diagnostic checks, not the missing protocol implementation or production readiness.

## Open acceptance gates

1. Implement and test actual validator orchestration against documented APIs with no mock success claims.
2. Add authenticated RPC integration, adversarial failure tests, and key lifecycle evidence before any network use.
3. Require independent security review, dependency audit, deployment controls and explicit release approval.
4. Resolve the approved-manifest private vs. actual-public repository visibility mismatch with the owner; do not change visibility automatically.

No gas, cycles, paid cloud resources, secrets, or public testnet/mainnet deployment are required for these checks.
