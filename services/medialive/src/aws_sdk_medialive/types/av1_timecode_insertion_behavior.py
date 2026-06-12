"""Generated from Smithy shape ``com.amazonaws.medialive#Av1TimecodeInsertionBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Av1 Timecode Insertion Behavior"""
Av1TimecodeInsertionBehavior: TypeAlias = Literal[
    "DISABLED",
    "METADATA_OBU",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "METADATA_OBU",
    )
)


def serialize_json(value: Av1TimecodeInsertionBehavior) -> str:
    return value


def deserialize_json(data: str) -> Av1TimecodeInsertionBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Av1TimecodeInsertionBehavior value: {data!r}"
        )
    return cast(Av1TimecodeInsertionBehavior, data)
