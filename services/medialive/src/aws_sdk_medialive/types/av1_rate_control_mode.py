"""Generated from Smithy shape ``com.amazonaws.medialive#Av1RateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Av1 Rate Control Mode"""
Av1RateControlMode: TypeAlias = Literal[
    "CBR",
    "QVBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CBR",
        "QVBR",
    )
)


def serialize_json(value: Av1RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Av1RateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Av1RateControlMode value: {data!r}")
    return cast(Av1RateControlMode, data)
