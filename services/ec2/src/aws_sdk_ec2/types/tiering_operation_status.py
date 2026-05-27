"""Generated from Smithy shape ``com.amazonaws.ec2#TieringOperationStatus``."""

from typing import Literal, TypeAlias

TieringOperationStatus: TypeAlias = Literal[
    "archival-in-progress",
    "archival-completed",
    "archival-failed",
    "temporary-restore-in-progress",
    "temporary-restore-completed",
    "temporary-restore-failed",
    "permanent-restore-in-progress",
    "permanent-restore-completed",
    "permanent-restore-failed",
]
