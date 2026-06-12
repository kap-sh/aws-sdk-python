"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ColorSpaceUsage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""There are two sources for color metadata, the input file and the job input settings Color space and HDR master display information settings. The Color space usage setting determines which takes precedence. Choose Force to use color metadata from the input job settings. If you don't specify values for those settings, the service defaults to using metadata from your input. FALLBACK - Choose Fallback to use color metadata from the source when it is present. If there's no color metadata in your input file, the service defaults to using values you specify in the input settings."""
ColorSpaceUsage: TypeAlias = Literal[
    "FORCE",
    "FALLBACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FORCE",
        "FALLBACK",
    )
)


def serialize_json(value: ColorSpaceUsage) -> str:
    return value


def deserialize_json(data: str) -> ColorSpaceUsage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColorSpaceUsage value: {data!r}")
    return cast(ColorSpaceUsage, data)
