"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CapabilitySyncStatus``."""

from typing import Literal, TypeAlias, cast

CapabilitySyncStatus: TypeAlias = Literal[
    "IN_SYNC",
    "OUT_OF_SYNC",
    "SYNC_FAILED",
    "UNKNOWN",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilitySyncStatus) -> str:
    return value


def deserialize_json(data: str) -> CapabilitySyncStatus:
    return cast(CapabilitySyncStatus, data)
