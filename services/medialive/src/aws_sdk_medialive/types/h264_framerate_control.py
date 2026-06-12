"""Generated from Smithy shape ``com.amazonaws.medialive#H264FramerateControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Framerate Control"""
H264FramerateControl: TypeAlias = Literal[
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


def serialize_json(value: H264FramerateControl) -> str:
    return value


def deserialize_json(data: str) -> H264FramerateControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264FramerateControl value: {data!r}")
    return cast(H264FramerateControl, data)
