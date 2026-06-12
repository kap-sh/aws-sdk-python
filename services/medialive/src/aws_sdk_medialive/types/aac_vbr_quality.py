"""Generated from Smithy shape ``com.amazonaws.medialive#AacVbrQuality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Aac Vbr Quality"""
AacVbrQuality: TypeAlias = Literal[
    "HIGH",
    "LOW",
    "MEDIUM_HIGH",
    "MEDIUM_LOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "LOW",
        "MEDIUM_HIGH",
        "MEDIUM_LOW",
    )
)


def serialize_json(value: AacVbrQuality) -> str:
    return value


def deserialize_json(data: str) -> AacVbrQuality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacVbrQuality value: {data!r}")
    return cast(AacVbrQuality, data)
