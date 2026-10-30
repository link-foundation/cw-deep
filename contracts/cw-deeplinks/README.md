# cw-deeplinks

This package is a deployable CosmWasm contract for DEEP Protocol. It is
distributed as a Wasm artifact, so registry publishing is intentionally disabled
with `publish = false` in `Cargo.toml`.

From the repository root, build the contract with `cargo wasm` after installing
the `wasm32-unknown-unknown` Rust target. The `rlib` target and `library` feature
remain available for local Rust integration.

Run `python3 experiments/check_publish_policy.py` to verify the registry policy.
