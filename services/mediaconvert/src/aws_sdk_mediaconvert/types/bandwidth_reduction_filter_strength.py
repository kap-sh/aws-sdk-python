"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BandwidthReductionFilterStrength``."""

from typing import Literal, TypeAlias, cast

"""Specify the strength of the Bandwidth reduction filter. For most workflows, we recommend that you choose Auto to reduce the bandwidth of your output with little to no perceptual decrease in video quality. For high quality and high bitrate outputs, choose Low. For the most bandwidth reduction, choose High. We recommend that you choose High for low bitrate outputs. Note that High may incur a slight increase in the softness of your output."""
BandwidthReductionFilterStrength: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "AUTO",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: BandwidthReductionFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> BandwidthReductionFilterStrength:
    return cast(BandwidthReductionFilterStrength, data)
