"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MLInputChannelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_PENDING",
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "ACTIVE",
        "DELETE_PENDING",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
        "INACTIVE",
    )
)


def serialize_json(value: MLInputChannelStatus) -> str:
    return value


def deserialize_json(data: str) -> MLInputChannelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MLInputChannelStatus value: {data!r}")
    return cast(MLInputChannelStatus, data)
