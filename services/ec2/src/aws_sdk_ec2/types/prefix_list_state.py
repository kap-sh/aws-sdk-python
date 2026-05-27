"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListState``."""

from typing import Literal, TypeAlias

PrefixListState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "modify-in-progress",
    "modify-complete",
    "modify-failed",
    "restore-in-progress",
    "restore-complete",
    "restore-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
]
