"""Generated from Smithy shape ``com.amazonaws.amplifybackend#MFAMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

MFAMode: TypeAlias = Literal[
    "ON",
    "OFF",
    "OPTIONAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON",
        "OFF",
        "OPTIONAL",
    )
)


def serialize_json(value: MFAMode) -> str:
    return value


def deserialize_json(data: str) -> MFAMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MFAMode value: {data!r}")
    return cast(MFAMode, data)
