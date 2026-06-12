"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionMapping``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Required when you set Dolby Vision Profile to Profile 8.1. When you set Content mapping to None, content mapping is not applied to the HDR10-compatible signal. Depending on the source peak nit level, clipping might occur on HDR devices without Dolby Vision. When you set Content mapping to HDR10 1000, the transcoder creates a 1,000 nits peak HDR10-compatible signal by applying static content mapping to the source. This mode is speed-optimized for PQ10 sources with metadata that is created from analysis. For graded Dolby Vision content, be aware that creative intent might not be guaranteed with extreme 1,000 nits trims."""
DolbyVisionMapping: TypeAlias = Literal[
    "HDR10_NOMAP",
    "HDR10_1000",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HDR10_NOMAP",
        "HDR10_1000",
    )
)


def serialize_json(value: DolbyVisionMapping) -> str:
    return value


def deserialize_json(data: str) -> DolbyVisionMapping:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DolbyVisionMapping value: {data!r}")
    return cast(DolbyVisionMapping, data)
