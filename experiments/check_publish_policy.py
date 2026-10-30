"""Verify that the deployable cw-deeplinks contract cannot be published to a registry."""

import json
from pathlib import Path
import subprocess


root = Path(__file__).resolve().parents[1]
metadata = json.loads(
    subprocess.check_output(
        ["cargo", "metadata", "--no-deps", "--format-version", "1", "--offline"],
        cwd=root,
        text=True,
    )
)
contract = next(package for package in metadata["packages"] if package["name"] == "cw-deeplinks")
assert contract["publish"] == [], (
    "cw-deeplinks is a deployable CosmWasm contract; "
    "set publish = false in contracts/cw-deeplinks/Cargo.toml"
)
print("cw-deeplinks registry publishing is disabled")
