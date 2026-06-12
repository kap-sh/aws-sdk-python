"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3SurroundExMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When encoding 3/2 audio, sets whether an extra center back surround channel is matrix encoded into the left and right surround channels."""
Eac3SurroundExMode: TypeAlias = Literal[
    "NOT_INDICATED",
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_INDICATED",
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: Eac3SurroundExMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3SurroundExMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3SurroundExMode value: {data!r}")
    return cast(Eac3SurroundExMode, data)
