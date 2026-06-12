"""Generated from Smithy shape ``com.amazonaws.medialive#BandwidthReductionFilterSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.bandwidth_reduction_filter_strength
    import aws_sdk_medialive.types.bandwidth_reduction_post_filter_sharpening


class BandwidthReductionFilterSettings(TypedDict):
    post_filter_sharpening: NotRequired[
        "aws_sdk_medialive.types.bandwidth_reduction_post_filter_sharpening.BandwidthReductionPostFilterSharpening"
    ]
    """Configures the sharpening control, which is available when the bandwidth reduction filter is enabled. This control sharpens edges and contours, which produces a specific artistic effect that you might want. We recommend that you test each of the values (including DISABLED) to observe the sharpening effect on the content."""
    strength: NotRequired[
        "aws_sdk_medialive.types.bandwidth_reduction_filter_strength.BandwidthReductionFilterStrength"
    ]
    """Enables the bandwidth reduction filter. The filter strengths range from 1 to 4. We recommend that you always enable this filter and use AUTO, to let MediaLive apply the optimum filtering for the context."""


# --- restJson1 ser/de ---
def serialize_json(value: BandwidthReductionFilterSettings) -> dict:
    out: dict = {}
    if "post_filter_sharpening" in value:
        import aws_sdk_medialive.types.bandwidth_reduction_post_filter_sharpening

        out["postFilterSharpening"] = (
            aws_sdk_medialive.types.bandwidth_reduction_post_filter_sharpening.serialize_json(
                value["post_filter_sharpening"]
            )
        )
    if "strength" in value:
        import aws_sdk_medialive.types.bandwidth_reduction_filter_strength

        out["strength"] = (
            aws_sdk_medialive.types.bandwidth_reduction_filter_strength.serialize_json(
                value["strength"]
            )
        )
    return out


def deserialize_json(data: dict) -> BandwidthReductionFilterSettings:
    out: BandwidthReductionFilterSettings = {}  # type: ignore[typeddict-item]
    if "postFilterSharpening" in data:
        import aws_sdk_medialive.types.bandwidth_reduction_post_filter_sharpening

        out["post_filter_sharpening"] = (
            aws_sdk_medialive.types.bandwidth_reduction_post_filter_sharpening.deserialize_json(
                data["postFilterSharpening"]
            )
        )
    if "strength" in data:
        import aws_sdk_medialive.types.bandwidth_reduction_filter_strength

        out["strength"] = (
            aws_sdk_medialive.types.bandwidth_reduction_filter_strength.deserialize_json(
                data["strength"]
            )
        )
    return out
