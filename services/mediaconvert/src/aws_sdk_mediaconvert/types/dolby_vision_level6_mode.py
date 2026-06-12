"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionLevel6Mode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Dolby Vision Mode to choose how the service will handle Dolby Vision MaxCLL and MaxFALL properies."""
DolbyVisionLevel6Mode: TypeAlias = Literal[
    "PASSTHROUGH",
    "RECALCULATE",
    "SPECIFY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "RECALCULATE",
        "SPECIFY",
    )
)


def serialize_json(value: DolbyVisionLevel6Mode) -> str:
    return value


def deserialize_json(data: str) -> DolbyVisionLevel6Mode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DolbyVisionLevel6Mode value: {data!r}")
    return cast(DolbyVisionLevel6Mode, data)
