"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotReturnCodes``."""

from typing import Literal, TypeAlias

SnapshotReturnCodes: TypeAlias = Literal[
    "success",
    "skipped",
    "missing-permissions",
    "internal-error",
    "client-error",
]
