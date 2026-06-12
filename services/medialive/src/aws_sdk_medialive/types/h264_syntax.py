"""Generated from Smithy shape ``com.amazonaws.medialive#H264Syntax``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Syntax"""
H264Syntax: TypeAlias = Literal[
    "DEFAULT",
    "RP2027",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "RP2027",
    )
)


def serialize_json(value: H264Syntax) -> str:
    return value


def deserialize_json(data: str) -> H264Syntax:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264Syntax value: {data!r}")
    return cast(H264Syntax, data)
