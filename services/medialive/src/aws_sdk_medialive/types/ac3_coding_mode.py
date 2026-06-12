"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3CodingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ac3 Coding Mode"""
Ac3CodingMode: TypeAlias = Literal[
    "CODING_MODE_1_0",
    "CODING_MODE_1_1",
    "CODING_MODE_2_0",
    "CODING_MODE_3_2_LFE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODING_MODE_1_0",
        "CODING_MODE_1_1",
        "CODING_MODE_2_0",
        "CODING_MODE_3_2_LFE",
    )
)


def serialize_json(value: Ac3CodingMode) -> str:
    return value


def deserialize_json(data: str) -> Ac3CodingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ac3CodingMode value: {data!r}")
    return cast(Ac3CodingMode, data)
