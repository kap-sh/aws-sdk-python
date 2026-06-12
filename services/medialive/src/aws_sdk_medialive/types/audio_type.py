"""Generated from Smithy shape ``com.amazonaws.medialive#AudioType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Type"""
AudioType: TypeAlias = Literal[
    "CLEAN_EFFECTS",
    "HEARING_IMPAIRED",
    "UNDEFINED",
    "VISUAL_IMPAIRED_COMMENTARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLEAN_EFFECTS",
        "HEARING_IMPAIRED",
        "UNDEFINED",
        "VISUAL_IMPAIRED_COMMENTARY",
    )
)


def serialize_json(value: AudioType) -> str:
    return value


def deserialize_json(data: str) -> AudioType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioType value: {data!r}")
    return cast(AudioType, data)
