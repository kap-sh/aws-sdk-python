"""Generated from Smithy shape ``com.amazonaws.medialive#InputCodec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""codec in increasing order of complexity"""
InputCodec: TypeAlias = Literal[
    "MPEG2",
    "AVC",
    "HEVC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MPEG2",
        "AVC",
        "HEVC",
    )
)


def serialize_json(value: InputCodec) -> str:
    return value


def deserialize_json(data: str) -> InputCodec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputCodec value: {data!r}")
    return cast(InputCodec, data)
