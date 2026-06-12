"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosCodingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""The coding mode for Dolby Digital Plus JOC (Atmos)."""
Eac3AtmosCodingMode: TypeAlias = Literal[
    "CODING_MODE_AUTO",
    "CODING_MODE_5_1_4",
    "CODING_MODE_7_1_4",
    "CODING_MODE_9_1_6",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODING_MODE_AUTO",
        "CODING_MODE_5_1_4",
        "CODING_MODE_7_1_4",
        "CODING_MODE_9_1_6",
    )
)


def serialize_json(value: Eac3AtmosCodingMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosCodingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3AtmosCodingMode value: {data!r}")
    return cast(Eac3AtmosCodingMode, data)
