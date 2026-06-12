"""Generated from Smithy shape ``com.amazonaws.medialive#CmafTimedMetadataPassthrough``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Cmaf Timed Metadata Passthrough"""
CmafTimedMetadataPassthrough: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: CmafTimedMetadataPassthrough) -> str:
    return value


def deserialize_json(data: str) -> CmafTimedMetadataPassthrough:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CmafTimedMetadataPassthrough value: {data!r}"
        )
    return cast(CmafTimedMetadataPassthrough, data)
