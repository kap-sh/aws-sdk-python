"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseReducerTemporalFilterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max4
    import aws_sdk_mediaconvert.types.__integer_min0_max16
    import aws_sdk_mediaconvert.types.__integer_min_negative1_max3
    import aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening
    import aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening_strength


class NoiseReducerTemporalFilterSettings(TypedDict, closed=True):
    aggressive_mode: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max4.__integerMin0Max4"
    ]
    """Use Aggressive mode for content that has complex motion. Higher values produce stronger temporal filtering. This filters highly complex scenes more aggressively and creates better VQ for low bitrate outputs."""
    post_temporal_sharpening: NotRequired[
        "aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening.NoiseFilterPostTemporalSharpening"
    ]
    """When you set Noise reducer to Temporal, the bandwidth and sharpness of your output is reduced. You can optionally use Post temporal sharpening to apply sharpening to the edges of your output. Note that Post temporal sharpening will also make the bandwidth reduction from the Noise reducer smaller. The default behavior, Auto, allows the transcoder to determine whether to apply sharpening, depending on your input type and quality. When you set Post temporal sharpening to Enabled, specify how much sharpening is applied using Post temporal sharpening strength. Set Post temporal sharpening to Disabled to not apply sharpening."""
    post_temporal_sharpening_strength: NotRequired[
        "aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening_strength.NoiseFilterPostTemporalSharpeningStrength"
    ]
    """Use Post temporal sharpening strength to define the amount of sharpening the transcoder applies to your output. Set Post temporal sharpening strength to Low, Medium, or High to indicate the amount of sharpening."""
    speed: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative1_max3.__integerMinNegative1Max3"
    ]
    """The speed of the filter (higher number is faster). Low setting reduces bit rate at the cost of transcode time, high setting improves transcode time at the cost of bit rate."""
    strength: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max16.__integerMin0Max16"
    ]
    """Specify the strength of the noise reducing filter on this output. Higher values produce stronger filtering. We recommend the following value ranges, depending on the result that you want: * 0-2 for complexity reduction with minimal sharpness loss * 2-8 for complexity reduction with image preservation * 8-16 for a high level of complexity reduction"""


# --- restJson1 ser/de ---
def serialize_json(value: NoiseReducerTemporalFilterSettings) -> dict:
    out: dict = {}
    if "aggressive_mode" in value:
        out["aggressiveMode"] = value["aggressive_mode"]
    if "post_temporal_sharpening" in value:
        import aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening

        out["postTemporalSharpening"] = (
            aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening.serialize_json(
                value["post_temporal_sharpening"]
            )
        )
    if "post_temporal_sharpening_strength" in value:
        import aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening_strength

        out["postTemporalSharpeningStrength"] = (
            aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening_strength.serialize_json(
                value["post_temporal_sharpening_strength"]
            )
        )
    if "speed" in value:
        out["speed"] = value["speed"]
    if "strength" in value:
        out["strength"] = value["strength"]
    return out


def deserialize_json(data: dict) -> NoiseReducerTemporalFilterSettings:
    out: NoiseReducerTemporalFilterSettings = {}  # type: ignore[typeddict-item]
    if "aggressiveMode" in data:
        out["aggressive_mode"] = data["aggressiveMode"]
    if "postTemporalSharpening" in data:
        import aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening

        out["post_temporal_sharpening"] = (
            aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening.deserialize_json(
                data["postTemporalSharpening"]
            )
        )
    if "postTemporalSharpeningStrength" in data:
        import aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening_strength

        out["post_temporal_sharpening_strength"] = (
            aws_sdk_mediaconvert.types.noise_filter_post_temporal_sharpening_strength.deserialize_json(
                data["postTemporalSharpeningStrength"]
            )
        )
    if "speed" in data:
        out["speed"] = data["speed"]
    if "strength" in data:
        out["strength"] = data["strength"]
    return out
