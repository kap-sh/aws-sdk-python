"""Generated from Smithy shape ``com.amazonaws.medialive#AacInputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Aac Input Type"""
AacInputType: TypeAlias = Literal[
    "BROADCASTER_MIXED_AD",
    "NORMAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BROADCASTER_MIXED_AD",
        "NORMAL",
    )
)


def serialize_json(value: AacInputType) -> str:
    return value


def deserialize_json(data: str) -> AacInputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacInputType value: {data!r}")
    return cast(AacInputType, data)
