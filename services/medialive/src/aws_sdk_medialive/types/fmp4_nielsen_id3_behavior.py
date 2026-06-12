"""Generated from Smithy shape ``com.amazonaws.medialive#Fmp4NielsenId3Behavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Fmp4 Nielsen Id3 Behavior"""
Fmp4NielsenId3Behavior: TypeAlias = Literal[
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


def serialize_json(value: Fmp4NielsenId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> Fmp4NielsenId3Behavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Fmp4NielsenId3Behavior value: {data!r}")
    return cast(Fmp4NielsenId3Behavior, data)
