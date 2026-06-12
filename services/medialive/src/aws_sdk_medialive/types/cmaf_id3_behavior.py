"""Generated from Smithy shape ``com.amazonaws.medialive#CmafId3Behavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Cmaf Id3 Behavior"""
CmafId3Behavior: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: CmafId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> CmafId3Behavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafId3Behavior value: {data!r}")
    return cast(CmafId3Behavior, data)
