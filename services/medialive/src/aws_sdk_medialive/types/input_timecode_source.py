"""Generated from Smithy shape ``com.amazonaws.medialive#InputTimecodeSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Documentation update needed"""
InputTimecodeSource: TypeAlias = Literal[
    "ZEROBASED",
    "EMBEDDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ZEROBASED",
        "EMBEDDED",
    )
)


def serialize_json(value: InputTimecodeSource) -> str:
    return value


def deserialize_json(data: str) -> InputTimecodeSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputTimecodeSource value: {data!r}")
    return cast(InputTimecodeSource, data)
