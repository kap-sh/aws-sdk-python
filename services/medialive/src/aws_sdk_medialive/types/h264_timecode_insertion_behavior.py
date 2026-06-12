"""Generated from Smithy shape ``com.amazonaws.medialive#H264TimecodeInsertionBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Timecode Insertion Behavior"""
H264TimecodeInsertionBehavior: TypeAlias = Literal[
    "DISABLED",
    "PIC_TIMING_SEI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "PIC_TIMING_SEI",
    )
)


def serialize_json(value: H264TimecodeInsertionBehavior) -> str:
    return value


def deserialize_json(data: str) -> H264TimecodeInsertionBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H264TimecodeInsertionBehavior value: {data!r}"
        )
    return cast(H264TimecodeInsertionBehavior, data)
