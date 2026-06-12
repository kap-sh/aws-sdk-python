"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BandwidthReductionFilterSharpening``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening."""
BandwidthReductionFilterSharpening: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "OFF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
        "OFF",
    )
)


def serialize_json(value: BandwidthReductionFilterSharpening) -> str:
    return value


def deserialize_json(data: str) -> BandwidthReductionFilterSharpening:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BandwidthReductionFilterSharpening value: {data!r}"
        )
    return cast(BandwidthReductionFilterSharpening, data)
