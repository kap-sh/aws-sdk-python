"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BandwidthReductionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.bandwidth_reduction_filter_sharpening
    import capo_mediaconvert.types.bandwidth_reduction_filter_strength


class BandwidthReductionFilter(TypedDict, closed=True):
    sharpening: NotRequired[
        "capo_mediaconvert.types.bandwidth_reduction_filter_sharpening.BandwidthReductionFilterSharpening"
    ]
    """Optionally specify the level of sharpening to apply when you use the Bandwidth reduction filter. Sharpening adds contrast to the edges of your video content and can reduce softness. Keep the default value Off to apply no sharpening. Set Sharpening strength to Low to apply a minimal amount of sharpening, or High to apply a maximum amount of sharpening."""
    strength: NotRequired[
        "capo_mediaconvert.types.bandwidth_reduction_filter_strength.BandwidthReductionFilterStrength"
    ]
    """Specify the strength of the Bandwidth reduction filter. For most workflows, we recommend that you choose Auto to reduce the bandwidth of your output with little to no perceptual decrease in video quality. For high quality and high bitrate outputs, choose Low. For the most bandwidth reduction, choose High. We recommend that you choose High for low bitrate outputs. Note that High may incur a slight increase in the softness of your output."""


# --- restJson1 ser/de ---
def serialize_json(value: BandwidthReductionFilter) -> dict:
    out: dict = {}
    if "sharpening" in value:
        import capo_mediaconvert.types.bandwidth_reduction_filter_sharpening

        out["sharpening"] = (
            capo_mediaconvert.types.bandwidth_reduction_filter_sharpening.serialize_json(
                value["sharpening"]
            )
        )
    if "strength" in value:
        import capo_mediaconvert.types.bandwidth_reduction_filter_strength

        out["strength"] = (
            capo_mediaconvert.types.bandwidth_reduction_filter_strength.serialize_json(
                value["strength"]
            )
        )
    return out


def deserialize_json(data: dict) -> BandwidthReductionFilter:
    out: BandwidthReductionFilter = {}  # type: ignore[typeddict-item]
    if "sharpening" in data:
        import capo_mediaconvert.types.bandwidth_reduction_filter_sharpening

        out["sharpening"] = (
            capo_mediaconvert.types.bandwidth_reduction_filter_sharpening.deserialize_json(
                data["sharpening"]
            )
        )
    if "strength" in data:
        import capo_mediaconvert.types.bandwidth_reduction_filter_strength

        out["strength"] = (
            capo_mediaconvert.types.bandwidth_reduction_filter_strength.deserialize_json(
                data["strength"]
            )
        )
    return out
