"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2TimecodeInsertionBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Mpeg2 Timecode Insertion Behavior"""
Mpeg2TimecodeInsertionBehavior: TypeAlias = Literal[
    "DISABLED",
    "GOP_TIMECODE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "GOP_TIMECODE",
    )
)


def serialize_json(value: Mpeg2TimecodeInsertionBehavior) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2TimecodeInsertionBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Mpeg2TimecodeInsertionBehavior value: {data!r}"
        )
    return cast(Mpeg2TimecodeInsertionBehavior, data)
