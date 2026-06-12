"""Generated from Smithy shape ``com.amazonaws.medialive#H265TimecodeInsertionBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Timecode Insertion Behavior"""
H265TimecodeInsertionBehavior: TypeAlias = Literal[
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


def serialize_json(value: H265TimecodeInsertionBehavior) -> str:
    return value


def deserialize_json(data: str) -> H265TimecodeInsertionBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265TimecodeInsertionBehavior value: {data!r}"
        )
    return cast(H265TimecodeInsertionBehavior, data)
