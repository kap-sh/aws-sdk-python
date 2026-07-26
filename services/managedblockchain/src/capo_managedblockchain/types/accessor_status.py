"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorStatus``."""

from typing import Literal, TypeAlias, cast

AccessorStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING_DELETION",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessorStatus) -> str:
    return value


def deserialize_json(data: str) -> AccessorStatus:
    return cast(AccessorStatus, data)
