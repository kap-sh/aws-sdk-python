"""Generated from Smithy shape ``com.amazonaws.medialive#HlsDirectoryStructure``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Directory Structure"""
HlsDirectoryStructure: TypeAlias = Literal[
    "SINGLE_DIRECTORY",
    "SUBDIRECTORY_PER_STREAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_DIRECTORY",
        "SUBDIRECTORY_PER_STREAM",
    )
)


def serialize_json(value: HlsDirectoryStructure) -> str:
    return value


def deserialize_json(data: str) -> HlsDirectoryStructure:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsDirectoryStructure value: {data!r}")
    return cast(HlsDirectoryStructure, data)
