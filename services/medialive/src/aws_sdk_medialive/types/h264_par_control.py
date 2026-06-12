"""Generated from Smithy shape ``com.amazonaws.medialive#H264ParControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Par Control"""
H264ParControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZE_FROM_SOURCE",
        "SPECIFIED",
    )
)


def serialize_json(value: H264ParControl) -> str:
    return value


def deserialize_json(data: str) -> H264ParControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264ParControl value: {data!r}")
    return cast(H264ParControl, data)
