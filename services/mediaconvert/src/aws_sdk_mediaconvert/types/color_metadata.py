"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ColorMetadata``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose Insert for this setting to include color metadata in this output. Choose Ignore to exclude color metadata from this output. If you don't specify a value, the service sets this to Insert by default."""
ColorMetadata: TypeAlias = Literal[
    "IGNORE",
    "INSERT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE",
        "INSERT",
    )
)


def serialize_json(value: ColorMetadata) -> str:
    return value


def deserialize_json(data: str) -> ColorMetadata:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColorMetadata value: {data!r}")
    return cast(ColorMetadata, data)
