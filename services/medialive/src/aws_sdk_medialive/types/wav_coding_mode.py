"""Generated from Smithy shape ``com.amazonaws.medialive#WavCodingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Wav Coding Mode"""
WavCodingMode: TypeAlias = Literal[
    "CODING_MODE_1_0",
    "CODING_MODE_2_0",
    "CODING_MODE_4_0",
    "CODING_MODE_8_0",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODING_MODE_1_0",
        "CODING_MODE_2_0",
        "CODING_MODE_4_0",
        "CODING_MODE_8_0",
    )
)


def serialize_json(value: WavCodingMode) -> str:
    return value


def deserialize_json(data: str) -> WavCodingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WavCodingMode value: {data!r}")
    return cast(WavCodingMode, data)
