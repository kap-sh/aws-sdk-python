"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoPreprocessor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.color_corrector
    import aws_sdk_mediaconvert.types.deinterlacer
    import aws_sdk_mediaconvert.types.dolby_vision
    import aws_sdk_mediaconvert.types.hdr10_plus
    import aws_sdk_mediaconvert.types.image_inserter
    import aws_sdk_mediaconvert.types.noise_reducer
    import aws_sdk_mediaconvert.types.partner_watermarking
    import aws_sdk_mediaconvert.types.timecode_burnin


class VideoPreprocessor(TypedDict):
    color_corrector: NotRequired[
        "aws_sdk_mediaconvert.types.color_corrector.ColorCorrector"
    ]
    """Use these settings to convert the color space or to modify properties such as hue and contrast for this output. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/converting-the-color-space.html."""
    deinterlacer: NotRequired["aws_sdk_mediaconvert.types.deinterlacer.Deinterlacer"]
    """Use the deinterlacer to produce smoother motion and a clearer picture. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-scan-type.html."""
    dolby_vision: NotRequired["aws_sdk_mediaconvert.types.dolby_vision.DolbyVision"]
    """Enable Dolby Vision feature to produce Dolby Vision compatible video output."""
    hdr10_plus: NotRequired["aws_sdk_mediaconvert.types.hdr10_plus.Hdr10Plus"]
    """Enable HDR10+ analysis and metadata injection. Compatible with HEVC only."""
    image_inserter: NotRequired[
        "aws_sdk_mediaconvert.types.image_inserter.ImageInserter"
    ]
    """Enable the Image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each output individually. This setting is disabled by default."""
    noise_reducer: NotRequired["aws_sdk_mediaconvert.types.noise_reducer.NoiseReducer"]
    """Enable the Noise reducer feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default. When you enable Noise reducer, you must also select a value for Noise reducer filter. For AVC outputs, when you include Noise reducer, you cannot include the Bandwidth reduction filter."""
    partner_watermarking: NotRequired[
        "aws_sdk_mediaconvert.types.partner_watermarking.PartnerWatermarking"
    ]
    """If you work with a third party video watermarking partner, use the group of settings that correspond with your watermarking partner to include watermarks in your output."""
    timecode_burnin: NotRequired[
        "aws_sdk_mediaconvert.types.timecode_burnin.TimecodeBurnin"
    ]
    """Settings for burning the output timecode and specified prefix into the output."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoPreprocessor) -> dict:
    out: dict = {}
    if "color_corrector" in value:
        import aws_sdk_mediaconvert.types.color_corrector

        out["colorCorrector"] = (
            aws_sdk_mediaconvert.types.color_corrector.serialize_json(
                value["color_corrector"]
            )
        )
    if "deinterlacer" in value:
        import aws_sdk_mediaconvert.types.deinterlacer

        out["deinterlacer"] = aws_sdk_mediaconvert.types.deinterlacer.serialize_json(
            value["deinterlacer"]
        )
    if "dolby_vision" in value:
        import aws_sdk_mediaconvert.types.dolby_vision

        out["dolbyVision"] = aws_sdk_mediaconvert.types.dolby_vision.serialize_json(
            value["dolby_vision"]
        )
    if "hdr10_plus" in value:
        import aws_sdk_mediaconvert.types.hdr10_plus

        out["hdr10Plus"] = aws_sdk_mediaconvert.types.hdr10_plus.serialize_json(
            value["hdr10_plus"]
        )
    if "image_inserter" in value:
        import aws_sdk_mediaconvert.types.image_inserter

        out["imageInserter"] = aws_sdk_mediaconvert.types.image_inserter.serialize_json(
            value["image_inserter"]
        )
    if "noise_reducer" in value:
        import aws_sdk_mediaconvert.types.noise_reducer

        out["noiseReducer"] = aws_sdk_mediaconvert.types.noise_reducer.serialize_json(
            value["noise_reducer"]
        )
    if "partner_watermarking" in value:
        import aws_sdk_mediaconvert.types.partner_watermarking

        out["partnerWatermarking"] = (
            aws_sdk_mediaconvert.types.partner_watermarking.serialize_json(
                value["partner_watermarking"]
            )
        )
    if "timecode_burnin" in value:
        import aws_sdk_mediaconvert.types.timecode_burnin

        out["timecodeBurnin"] = (
            aws_sdk_mediaconvert.types.timecode_burnin.serialize_json(
                value["timecode_burnin"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoPreprocessor:
    out: VideoPreprocessor = {}  # type: ignore[typeddict-item]
    if "colorCorrector" in data:
        import aws_sdk_mediaconvert.types.color_corrector

        out["color_corrector"] = (
            aws_sdk_mediaconvert.types.color_corrector.deserialize_json(
                data["colorCorrector"]
            )
        )
    if "deinterlacer" in data:
        import aws_sdk_mediaconvert.types.deinterlacer

        out["deinterlacer"] = aws_sdk_mediaconvert.types.deinterlacer.deserialize_json(
            data["deinterlacer"]
        )
    if "dolbyVision" in data:
        import aws_sdk_mediaconvert.types.dolby_vision

        out["dolby_vision"] = aws_sdk_mediaconvert.types.dolby_vision.deserialize_json(
            data["dolbyVision"]
        )
    if "hdr10Plus" in data:
        import aws_sdk_mediaconvert.types.hdr10_plus

        out["hdr10_plus"] = aws_sdk_mediaconvert.types.hdr10_plus.deserialize_json(
            data["hdr10Plus"]
        )
    if "imageInserter" in data:
        import aws_sdk_mediaconvert.types.image_inserter

        out["image_inserter"] = (
            aws_sdk_mediaconvert.types.image_inserter.deserialize_json(
                data["imageInserter"]
            )
        )
    if "noiseReducer" in data:
        import aws_sdk_mediaconvert.types.noise_reducer

        out["noise_reducer"] = (
            aws_sdk_mediaconvert.types.noise_reducer.deserialize_json(
                data["noiseReducer"]
            )
        )
    if "partnerWatermarking" in data:
        import aws_sdk_mediaconvert.types.partner_watermarking

        out["partner_watermarking"] = (
            aws_sdk_mediaconvert.types.partner_watermarking.deserialize_json(
                data["partnerWatermarking"]
            )
        )
    if "timecodeBurnin" in data:
        import aws_sdk_mediaconvert.types.timecode_burnin

        out["timecode_burnin"] = (
            aws_sdk_mediaconvert.types.timecode_burnin.deserialize_json(
                data["timecodeBurnin"]
            )
        )
    return out
