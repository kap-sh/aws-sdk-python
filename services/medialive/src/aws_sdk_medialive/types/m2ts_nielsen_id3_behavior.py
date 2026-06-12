"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsNielsenId3Behavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Nielsen Id3 Behavior"""
M2tsNielsenId3Behavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PASSTHROUGH",
        "PASSTHROUGH",
    )
)


def serialize_json(value: M2tsNielsenId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> M2tsNielsenId3Behavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsNielsenId3Behavior value: {data!r}")
    return cast(M2tsNielsenId3Behavior, data)
