"""Generated from Smithy shape ``com.amazonaws.medialive#AacRawFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Aac Raw Format"""
AacRawFormat: TypeAlias = Literal[
    "LATM_LOAS",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATM_LOAS",
        "NONE",
    )
)


def serialize_json(value: AacRawFormat) -> str:
    return value


def deserialize_json(data: str) -> AacRawFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacRawFormat value: {data!r}")
    return cast(AacRawFormat, data)
