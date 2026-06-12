"""Generated from Smithy shape ``com.amazonaws.medialive#CmafNielsenId3Behavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Cmaf Nielsen Id3 Behavior"""
CmafNielsenId3Behavior: TypeAlias = Literal[
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


def serialize_json(value: CmafNielsenId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> CmafNielsenId3Behavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafNielsenId3Behavior value: {data!r}")
    return cast(CmafNielsenId3Behavior, data)
