"""Generated from Smithy shape ``com.amazonaws.mediaconvert#RequiredFlag``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Set to ENABLED to force a rendition to be included."""
RequiredFlag: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: RequiredFlag) -> str:
    return value


def deserialize_json(data: str) -> RequiredFlag:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RequiredFlag value: {data!r}")
    return cast(RequiredFlag, data)
