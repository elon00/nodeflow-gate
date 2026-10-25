# Security status — unverified

This repository currently contains a **local deterministic diagnostic**, not a secure validator orchestrator. It has **no FIPS-validated PQC implementation**, no TLS certification, no production cryptographic protocol, and no independent security approval.

Do not use the local state mixer as a hash, CSPRNG, signature, KEM, nonce generator, or security boundary. Do not deploy or manage funds based on these diagnostics.

Before production acceptance, require real authenticated RPC/validator functionality, failure and adversarial tests, key/nonce lifecycle review, supply-chain and dependency assessment, threat model, and independent security review. Keep security gates fail-closed. Report findings privately to the repository owner through an established trusted channel; no bounty payment is promised.
