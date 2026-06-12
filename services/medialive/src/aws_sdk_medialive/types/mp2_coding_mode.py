"""Generated from Smithy shape ``com.amazonaws.medialive#Mp2CodingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Mp2 Coding Mode"""
Mp2CodingMode: TypeAlias = Literal[
    "CODING_MODE_1_0",
    "CODING_MODE_2_0",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODING_MODE_1_0",
        "CODING_MODE_2_0",
    )
)


def serialize_json(value: Mp2CodingMode) -> str:
    return value


def deserialize_json(data: str) -> Mp2CodingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mp2CodingMode value: {data!r}")
    return cast(Mp2CodingMode, data)
