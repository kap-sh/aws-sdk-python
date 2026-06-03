"""Generated from Smithy shape ``com.amazonaws.kms#KeyState``."""

from typing import Literal, TypeAlias

KeyState: TypeAlias = Literal[
    "Creating",
    "Enabled",
    "Disabled",
    "PendingDeletion",
    "PendingImport",
    "PendingReplicaDeletion",
    "Unavailable",
    "Updating",
]
