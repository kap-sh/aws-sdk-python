"""Generated from Smithy shape ``com.amazonaws.medialive#AacCodingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Aac Coding Mode"""
AacCodingMode: TypeAlias = Literal[
    "AD_RECEIVER_MIX",
    "CODING_MODE_1_0",
    "CODING_MODE_1_1",
    "CODING_MODE_2_0",
    "CODING_MODE_5_1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AD_RECEIVER_MIX",
        "CODING_MODE_1_0",
        "CODING_MODE_1_1",
        "CODING_MODE_2_0",
        "CODING_MODE_5_1",
    )
)


def serialize_json(value: AacCodingMode) -> str:
    return value


def deserialize_json(data: str) -> AacCodingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacCodingMode value: {data!r}")
    return cast(AacCodingMode, data)
