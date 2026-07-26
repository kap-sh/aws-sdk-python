"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputGroupType``."""

from typing import Literal, TypeAlias, cast

"""Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth Streaming, CMAF)"""
OutputGroupType: TypeAlias = Literal[
    "HLS_GROUP_SETTINGS",
    "DASH_ISO_GROUP_SETTINGS",
    "FILE_GROUP_SETTINGS",
    "MS_SMOOTH_GROUP_SETTINGS",
    "CMAF_GROUP_SETTINGS",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputGroupType) -> str:
    return value


def deserialize_json(data: str) -> OutputGroupType:
    return cast(OutputGroupType, data)
