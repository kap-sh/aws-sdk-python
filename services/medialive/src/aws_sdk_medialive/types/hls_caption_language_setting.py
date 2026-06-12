"""Generated from Smithy shape ``com.amazonaws.medialive#HlsCaptionLanguageSetting``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Caption Language Setting"""
HlsCaptionLanguageSetting: TypeAlias = Literal[
    "INSERT",
    "NONE",
    "OMIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSERT",
        "NONE",
        "OMIT",
    )
)


def serialize_json(value: HlsCaptionLanguageSetting) -> str:
    return value


def deserialize_json(data: str) -> HlsCaptionLanguageSetting:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsCaptionLanguageSetting value: {data!r}")
    return cast(HlsCaptionLanguageSetting, data)
