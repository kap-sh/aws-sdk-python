"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputGroupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth Streaming, CMAF)"""
OutputGroupType: TypeAlias = Literal[
    "HLS_GROUP_SETTINGS",
    "DASH_ISO_GROUP_SETTINGS",
    "FILE_GROUP_SETTINGS",
    "MS_SMOOTH_GROUP_SETTINGS",
    "CMAF_GROUP_SETTINGS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HLS_GROUP_SETTINGS",
        "DASH_ISO_GROUP_SETTINGS",
        "FILE_GROUP_SETTINGS",
        "MS_SMOOTH_GROUP_SETTINGS",
        "CMAF_GROUP_SETTINGS",
    )
)


def serialize_json(value: OutputGroupType) -> str:
    return value


def deserialize_json(data: str) -> OutputGroupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputGroupType value: {data!r}")
    return cast(OutputGroupType, data)
