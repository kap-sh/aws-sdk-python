"""Generated from Smithy shape ``com.amazonaws.medialive#HlsTsFileMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Ts File Mode"""
HlsTsFileMode: TypeAlias = Literal[
    "SEGMENTED_FILES",
    "SINGLE_FILE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEGMENTED_FILES",
        "SINGLE_FILE",
    )
)


def serialize_json(value: HlsTsFileMode) -> str:
    return value


def deserialize_json(data: str) -> HlsTsFileMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsTsFileMode value: {data!r}")
    return cast(HlsTsFileMode, data)
