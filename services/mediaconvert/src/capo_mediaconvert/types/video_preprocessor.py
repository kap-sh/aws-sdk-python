"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoPreprocessor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.color_corrector
    import capo_mediaconvert.types.deinterlacer
    import capo_mediaconvert.types.dolby_vision
    import capo_mediaconvert.types.hdr10_plus
    import capo_mediaconvert.types.image_inserter
    import capo_mediaconvert.types.noise_reducer
    import capo_mediaconvert.types.partner_watermarking
    import capo_mediaconvert.types.timecode_burnin


class VideoPreprocessor(TypedDict, closed=True):
    color_corrector: NotRequired[
        "capo_mediaconvert.types.color_corrector.ColorCorrector"
    ]
    """Use these settings to convert the color space or to modify properties such as hue and contrast for this output. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/converting-the-color-space.html."""
    deinterlacer: NotRequired["capo_mediaconvert.types.deinterlacer.Deinterlacer"]
    """Use the deinterlacer to produce smoother motion and a clearer picture. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-scan-type.html."""
    dolby_vision: NotRequired["capo_mediaconvert.types.dolby_vision.DolbyVision"]
    """Enable Dolby Vision feature to produce Dolby Vision compatible video output."""
    hdr10_plus: NotRequired["capo_mediaconvert.types.hdr10_plus.Hdr10Plus"]
    """Enable HDR10+ analysis and metadata injection. Compatible with HEVC only."""
    image_inserter: NotRequired["capo_mediaconvert.types.image_inserter.ImageInserter"]
    """Enable the Image inserter feature to include a graphic overlay on your video. Enable or disable this feature for each output individually. This setting is disabled by default."""
    noise_reducer: NotRequired["capo_mediaconvert.types.noise_reducer.NoiseReducer"]
    """Enable the Noise reducer feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default. When you enable Noise reducer, you must also select a value for Noise reducer filter. For AVC outputs, when you include Noise reducer, you cannot include the Bandwidth reduction filter."""
    partner_watermarking: NotRequired[
        "capo_mediaconvert.types.partner_watermarking.PartnerWatermarking"
    ]
    """If you work with a third party video watermarking partner, use the group of settings that correspond with your watermarking partner to include watermarks in your output."""
    timecode_burnin: NotRequired[
        "capo_mediaconvert.types.timecode_burnin.TimecodeBurnin"
    ]
    """Settings for burning the output timecode and specified prefix into the output."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoPreprocessor) -> dict:
    out: dict = {}
    if "color_corrector" in value:
        import capo_mediaconvert.types.color_corrector

        out["colorCorrector"] = capo_mediaconvert.types.color_corrector.serialize_json(
            value["color_corrector"]
        )
    if "deinterlacer" in value:
        import capo_mediaconvert.types.deinterlacer

        out["deinterlacer"] = capo_mediaconvert.types.deinterlacer.serialize_json(
            value["deinterlacer"]
        )
    if "dolby_vision" in value:
        import capo_mediaconvert.types.dolby_vision

        out["dolbyVision"] = capo_mediaconvert.types.dolby_vision.serialize_json(
            value["dolby_vision"]
        )
    if "hdr10_plus" in value:
        import capo_mediaconvert.types.hdr10_plus

        out["hdr10Plus"] = capo_mediaconvert.types.hdr10_plus.serialize_json(
            value["hdr10_plus"]
        )
    if "image_inserter" in value:
        import capo_mediaconvert.types.image_inserter

        out["imageInserter"] = capo_mediaconvert.types.image_inserter.serialize_json(
            value["image_inserter"]
        )
    if "noise_reducer" in value:
        import capo_mediaconvert.types.noise_reducer

        out["noiseReducer"] = capo_mediaconvert.types.noise_reducer.serialize_json(
            value["noise_reducer"]
        )
    if "partner_watermarking" in value:
        import capo_mediaconvert.types.partner_watermarking

        out["partnerWatermarking"] = (
            capo_mediaconvert.types.partner_watermarking.serialize_json(
                value["partner_watermarking"]
            )
        )
    if "timecode_burnin" in value:
        import capo_mediaconvert.types.timecode_burnin

        out["timecodeBurnin"] = capo_mediaconvert.types.timecode_burnin.serialize_json(
            value["timecode_burnin"]
        )
    return out


def deserialize_json(data: dict) -> VideoPreprocessor:
    out: VideoPreprocessor = {}  # type: ignore[typeddict-item]
    if "colorCorrector" in data:
        import capo_mediaconvert.types.color_corrector

        out["color_corrector"] = (
            capo_mediaconvert.types.color_corrector.deserialize_json(
                data["colorCorrector"]
            )
        )
    if "deinterlacer" in data:
        import capo_mediaconvert.types.deinterlacer

        out["deinterlacer"] = capo_mediaconvert.types.deinterlacer.deserialize_json(
            data["deinterlacer"]
        )
    if "dolbyVision" in data:
        import capo_mediaconvert.types.dolby_vision

        out["dolby_vision"] = capo_mediaconvert.types.dolby_vision.deserialize_json(
            data["dolbyVision"]
        )
    if "hdr10Plus" in data:
        import capo_mediaconvert.types.hdr10_plus

        out["hdr10_plus"] = capo_mediaconvert.types.hdr10_plus.deserialize_json(
            data["hdr10Plus"]
        )
    if "imageInserter" in data:
        import capo_mediaconvert.types.image_inserter

        out["image_inserter"] = capo_mediaconvert.types.image_inserter.deserialize_json(
            data["imageInserter"]
        )
    if "noiseReducer" in data:
        import capo_mediaconvert.types.noise_reducer

        out["noise_reducer"] = capo_mediaconvert.types.noise_reducer.deserialize_json(
            data["noiseReducer"]
        )
    if "partnerWatermarking" in data:
        import capo_mediaconvert.types.partner_watermarking

        out["partner_watermarking"] = (
            capo_mediaconvert.types.partner_watermarking.deserialize_json(
                data["partnerWatermarking"]
            )
        )
    if "timecodeBurnin" in data:
        import capo_mediaconvert.types.timecode_burnin

        out["timecode_burnin"] = (
            capo_mediaconvert.types.timecode_burnin.deserialize_json(
                data["timecodeBurnin"]
            )
        )
    return out
