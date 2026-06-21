"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BandwidthReductionFilterSharpening``."""

from typing import Literal, TypeAlias, cast

"""Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening."""
BandwidthReductionFilterSharpening: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: BandwidthReductionFilterSharpening) -> str:
    return value


def deserialize_json(data: str) -> BandwidthReductionFilterSharpening:
    return cast(BandwidthReductionFilterSharpening, data)
