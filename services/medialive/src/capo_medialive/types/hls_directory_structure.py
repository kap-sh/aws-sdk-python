"""Generated from Smithy shape ``com.amazonaws.medialive#HlsDirectoryStructure``."""

from typing import Literal, TypeAlias, cast

"""Hls Directory Structure"""
HlsDirectoryStructure: TypeAlias = Literal[
    "SINGLE_DIRECTORY",
    "SUBDIRECTORY_PER_STREAM",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsDirectoryStructure) -> str:
    return value


def deserialize_json(data: str) -> HlsDirectoryStructure:
    return cast(HlsDirectoryStructure, data)
