"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovClapAtom``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When enabled, include 'clap' atom if appropriate for the video output settings."""
MovClapAtom: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: MovClapAtom) -> str:
    return value


def deserialize_json(data: str) -> MovClapAtom:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MovClapAtom value: {data!r}")
    return cast(MovClapAtom, data)
