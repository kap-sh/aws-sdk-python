"""Generated from Smithy shape ``com.amazonaws.medialive#AacRateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Aac Rate Control Mode"""
AacRateControlMode: TypeAlias = Literal[
    "CBR",
    "VBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CBR",
        "VBR",
    )
)


def serialize_json(value: AacRateControlMode) -> str:
    return value


def deserialize_json(data: str) -> AacRateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacRateControlMode value: {data!r}")
    return cast(AacRateControlMode, data)
