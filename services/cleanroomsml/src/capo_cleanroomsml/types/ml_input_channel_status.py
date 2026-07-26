"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MLInputChannelStatus``."""

from typing import Literal, TypeAlias, cast

MLInputChannelStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETE_PENDING",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MLInputChannelStatus) -> str:
    return value


def deserialize_json(data: str) -> MLInputChannelStatus:
    return cast(MLInputChannelStatus, data)
