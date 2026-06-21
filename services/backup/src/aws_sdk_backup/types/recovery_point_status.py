"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointStatus``."""

from typing import Literal, TypeAlias, cast

RecoveryPointStatus: TypeAlias = Literal[
    "COMPLETED",
    "PARTIAL",
    "DELETING",
    "EXPIRED",
    "AVAILABLE",
    "STOPPED",
    "CREATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointStatus) -> str:
    return value


def deserialize_json(data: str) -> RecoveryPointStatus:
    return cast(RecoveryPointStatus, data)
