"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer_min0
    import aws_sdk_medialive.types.__integer_min0_max7
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.afd_signaling
    import aws_sdk_medialive.types.fixed_afd
    import aws_sdk_medialive.types.mpeg2_adaptive_quantization
    import aws_sdk_medialive.types.mpeg2_color_metadata
    import aws_sdk_medialive.types.mpeg2_color_space
    import aws_sdk_medialive.types.mpeg2_display_ratio
    import aws_sdk_medialive.types.mpeg2_filter_settings
    import aws_sdk_medialive.types.mpeg2_gop_size_units
    import aws_sdk_medialive.types.mpeg2_scan_type
    import aws_sdk_medialive.types.mpeg2_sub_gop_length
    import aws_sdk_medialive.types.mpeg2_timecode_insertion_behavior
    import aws_sdk_medialive.types.timecode_burnin_settings


class Mpeg2Settings(TypedDict):
    adaptive_quantization: NotRequired[
        "aws_sdk_medialive.types.mpeg2_adaptive_quantization.Mpeg2AdaptiveQuantization"
    ]
    """Choose Off to disable adaptive quantization. Or choose another value to enable the quantizer and set its strength. The strengths are: Auto, Off, Low, Medium, High. When you enable this field, MediaLive allows intra-frame quantizers to vary, which might improve visual quality."""
    afd_signaling: NotRequired["aws_sdk_medialive.types.afd_signaling.AfdSignaling"]
    """Indicates the AFD values that MediaLive will write into the video encode. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose AUTO. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: MediaLive will use the value you specify in fixedAFD."""
    color_metadata: NotRequired[
        "aws_sdk_medialive.types.mpeg2_color_metadata.Mpeg2ColorMetadata"
    ]
    """Specifies whether to include the color space metadata. The metadata describes the color space that applies to the video (the colorSpace field). We recommend that you insert the metadata."""
    color_space: NotRequired[
        "aws_sdk_medialive.types.mpeg2_color_space.Mpeg2ColorSpace"
    ]
    r"""Choose the type of color space conversion to apply to the output. For detailed information on setting up both the input and the output to obtain the desired color space in the output, see the section on \\"MediaLive Features - Video - color space\\" in the MediaLive User Guide. PASSTHROUGH: Keep the color space of the input content - do not convert it. AUTO:Convert all content that is SD to rec 601, and convert all content that is HD to rec 709."""
    display_aspect_ratio: NotRequired[
        "aws_sdk_medialive.types.mpeg2_display_ratio.Mpeg2DisplayRatio"
    ]
    """Sets the pixel aspect ratio for the encode."""
    filter_settings: NotRequired[
        "aws_sdk_medialive.types.mpeg2_filter_settings.Mpeg2FilterSettings"
    ]
    """Optionally specify a noise reduction filter, which can improve quality of compressed content. If you do not choose a filter, no filter will be applied. TEMPORAL: This filter is useful for both source content that is noisy (when it has excessive digital artifacts) and source content that is clean. When the content is noisy, the filter cleans up the source content before the encoding phase, with these two effects: First, it improves the output video quality because the content has been cleaned up. Secondly, it decreases the bandwidth because MediaLive does not waste bits on encoding noise. When the content is reasonably clean, the filter tends to decrease the bitrate."""
    fixed_afd: NotRequired["aws_sdk_medialive.types.fixed_afd.FixedAfd"]
    """Complete this field only when afdSignaling is set to FIXED. Enter the AFD value (4 bits) to write on all frames of the video encode."""
    framerate_denominator: NotRequired[
        "aws_sdk_medialive.types.__integer_min1.__integerMin1"
    ]
    r"""description\": \"The framerate denominator. For example, 1001. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS."""
    framerate_numerator: NotRequired[
        "aws_sdk_medialive.types.__integer_min1.__integerMin1"
    ]
    """The framerate numerator. For example, 24000. The framerate is the numerator divided by the denominator. For example, 24000 / 1001 = 23.976 FPS."""
    gop_closed_cadence: NotRequired[
        "aws_sdk_medialive.types.__integer_min0.__integerMin0"
    ]
    """MPEG2: default is open GOP."""
    gop_num_b_frames: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max7.__integerMin0Max7"
    ]
    """Relates to the GOP structure. The number of B-frames between reference frames. If you do not know what a B-frame is, use the default."""
    gop_size: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Relates to the GOP structure. The GOP size (keyframe interval) in the units specified in gopSizeUnits. If you do not know what GOP is, use the default. If gopSizeUnits is frames, then the gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, the gopSize must be greater than 0, but does not need to be an integer."""
    gop_size_units: NotRequired[
        "aws_sdk_medialive.types.mpeg2_gop_size_units.Mpeg2GopSizeUnits"
    ]
    """Relates to the GOP structure. Specifies whether the gopSize is specified in frames or seconds. If you do not plan to change the default gopSize, leave the default. If you specify SECONDS, MediaLive will internally convert the gop size to a frame count."""
    scan_type: NotRequired["aws_sdk_medialive.types.mpeg2_scan_type.Mpeg2ScanType"]
    """Set the scan type of the output to PROGRESSIVE or INTERLACED (top field first)."""
    subgop_length: NotRequired[
        "aws_sdk_medialive.types.mpeg2_sub_gop_length.Mpeg2SubGopLength"
    ]
    """Relates to the GOP structure. If you do not know what GOP is, use the default. FIXED: Set the number of B-frames in each sub-GOP to the value in gopNumBFrames. DYNAMIC: Let MediaLive optimize the number of B-frames in each sub-GOP, to improve visual quality."""
    timecode_insertion: NotRequired[
        "aws_sdk_medialive.types.mpeg2_timecode_insertion_behavior.Mpeg2TimecodeInsertionBehavior"
    ]
    r"""Determines how MediaLive inserts timecodes in the output video. For detailed information about setting up the input and the output for a timecode, see the section on \\"MediaLive Features - Timecode configuration\\" in the MediaLive User Guide. DISABLED: do not include timecodes. GOP_TIMECODE: Include timecode metadata in the GOP header."""
    timecode_burnin_settings: NotRequired[
        "aws_sdk_medialive.types.timecode_burnin_settings.TimecodeBurninSettings"
    ]
    """Timecode burn-in settings"""


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2Settings) -> dict:
    out: dict = {}
    if "adaptive_quantization" in value:
        import aws_sdk_medialive.types.mpeg2_adaptive_quantization

        out["adaptiveQuantization"] = (
            aws_sdk_medialive.types.mpeg2_adaptive_quantization.serialize_json(
                value["adaptive_quantization"]
            )
        )
    if "afd_signaling" in value:
        import aws_sdk_medialive.types.afd_signaling

        out["afdSignaling"] = aws_sdk_medialive.types.afd_signaling.serialize_json(
            value["afd_signaling"]
        )
    if "color_metadata" in value:
        import aws_sdk_medialive.types.mpeg2_color_metadata

        out["colorMetadata"] = (
            aws_sdk_medialive.types.mpeg2_color_metadata.serialize_json(
                value["color_metadata"]
            )
        )
    if "color_space" in value:
        import aws_sdk_medialive.types.mpeg2_color_space

        out["colorSpace"] = aws_sdk_medialive.types.mpeg2_color_space.serialize_json(
            value["color_space"]
        )
    if "display_aspect_ratio" in value:
        import aws_sdk_medialive.types.mpeg2_display_ratio

        out["displayAspectRatio"] = (
            aws_sdk_medialive.types.mpeg2_display_ratio.serialize_json(
                value["display_aspect_ratio"]
            )
        )
    if "filter_settings" in value:
        import aws_sdk_medialive.types.mpeg2_filter_settings

        out["filterSettings"] = (
            aws_sdk_medialive.types.mpeg2_filter_settings.serialize_json(
                value["filter_settings"]
            )
        )
    if "fixed_afd" in value:
        import aws_sdk_medialive.types.fixed_afd

        out["fixedAfd"] = aws_sdk_medialive.types.fixed_afd.serialize_json(
            value["fixed_afd"]
        )
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "gop_closed_cadence" in value:
        out["gopClosedCadence"] = value["gop_closed_cadence"]
    if "gop_num_b_frames" in value:
        out["gopNumBFrames"] = value["gop_num_b_frames"]
    if "gop_size" in value:
        out["gopSize"] = value["gop_size"]
    if "gop_size_units" in value:
        import aws_sdk_medialive.types.mpeg2_gop_size_units

        out["gopSizeUnits"] = (
            aws_sdk_medialive.types.mpeg2_gop_size_units.serialize_json(
                value["gop_size_units"]
            )
        )
    if "scan_type" in value:
        import aws_sdk_medialive.types.mpeg2_scan_type

        out["scanType"] = aws_sdk_medialive.types.mpeg2_scan_type.serialize_json(
            value["scan_type"]
        )
    if "subgop_length" in value:
        import aws_sdk_medialive.types.mpeg2_sub_gop_length

        out["subgopLength"] = (
            aws_sdk_medialive.types.mpeg2_sub_gop_length.serialize_json(
                value["subgop_length"]
            )
        )
    if "timecode_insertion" in value:
        import aws_sdk_medialive.types.mpeg2_timecode_insertion_behavior

        out["timecodeInsertion"] = (
            aws_sdk_medialive.types.mpeg2_timecode_insertion_behavior.serialize_json(
                value["timecode_insertion"]
            )
        )
    if "timecode_burnin_settings" in value:
        import aws_sdk_medialive.types.timecode_burnin_settings

        out["timecodeBurninSettings"] = (
            aws_sdk_medialive.types.timecode_burnin_settings.serialize_json(
                value["timecode_burnin_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Mpeg2Settings:
    out: Mpeg2Settings = {}  # type: ignore[typeddict-item]
    if "adaptiveQuantization" in data:
        import aws_sdk_medialive.types.mpeg2_adaptive_quantization

        out["adaptive_quantization"] = (
            aws_sdk_medialive.types.mpeg2_adaptive_quantization.deserialize_json(
                data["adaptiveQuantization"]
            )
        )
    if "afdSignaling" in data:
        import aws_sdk_medialive.types.afd_signaling

        out["afd_signaling"] = aws_sdk_medialive.types.afd_signaling.deserialize_json(
            data["afdSignaling"]
        )
    if "colorMetadata" in data:
        import aws_sdk_medialive.types.mpeg2_color_metadata

        out["color_metadata"] = (
            aws_sdk_medialive.types.mpeg2_color_metadata.deserialize_json(
                data["colorMetadata"]
            )
        )
    if "colorSpace" in data:
        import aws_sdk_medialive.types.mpeg2_color_space

        out["color_space"] = aws_sdk_medialive.types.mpeg2_color_space.deserialize_json(
            data["colorSpace"]
        )
    if "displayAspectRatio" in data:
        import aws_sdk_medialive.types.mpeg2_display_ratio

        out["display_aspect_ratio"] = (
            aws_sdk_medialive.types.mpeg2_display_ratio.deserialize_json(
                data["displayAspectRatio"]
            )
        )
    if "filterSettings" in data:
        import aws_sdk_medialive.types.mpeg2_filter_settings

        out["filter_settings"] = (
            aws_sdk_medialive.types.mpeg2_filter_settings.deserialize_json(
                data["filterSettings"]
            )
        )
    if "fixedAfd" in data:
        import aws_sdk_medialive.types.fixed_afd

        out["fixed_afd"] = aws_sdk_medialive.types.fixed_afd.deserialize_json(
            data["fixedAfd"]
        )
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "gopClosedCadence" in data:
        out["gop_closed_cadence"] = data["gopClosedCadence"]
    if "gopNumBFrames" in data:
        out["gop_num_b_frames"] = data["gopNumBFrames"]
    if "gopSize" in data:
        out["gop_size"] = data["gopSize"]
    if "gopSizeUnits" in data:
        import aws_sdk_medialive.types.mpeg2_gop_size_units

        out["gop_size_units"] = (
            aws_sdk_medialive.types.mpeg2_gop_size_units.deserialize_json(
                data["gopSizeUnits"]
            )
        )
    if "scanType" in data:
        import aws_sdk_medialive.types.mpeg2_scan_type

        out["scan_type"] = aws_sdk_medialive.types.mpeg2_scan_type.deserialize_json(
            data["scanType"]
        )
    if "subgopLength" in data:
        import aws_sdk_medialive.types.mpeg2_sub_gop_length

        out["subgop_length"] = (
            aws_sdk_medialive.types.mpeg2_sub_gop_length.deserialize_json(
                data["subgopLength"]
            )
        )
    if "timecodeInsertion" in data:
        import aws_sdk_medialive.types.mpeg2_timecode_insertion_behavior

        out["timecode_insertion"] = (
            aws_sdk_medialive.types.mpeg2_timecode_insertion_behavior.deserialize_json(
                data["timecodeInsertion"]
            )
        )
    if "timecodeBurninSettings" in data:
        import aws_sdk_medialive.types.timecode_burnin_settings

        out["timecode_burnin_settings"] = (
            aws_sdk_medialive.types.timecode_burnin_settings.deserialize_json(
                data["timecodeBurninSettings"]
            )
        )
    return out
