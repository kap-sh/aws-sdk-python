"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min1_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647
    import aws_sdk_mediaconvert.types.__list_of__integer_min1_max2147483647
    import aws_sdk_mediaconvert.types.alpha_behavior
    import aws_sdk_mediaconvert.types.color_space
    import aws_sdk_mediaconvert.types.color_space_usage
    import aws_sdk_mediaconvert.types.embedded_timecode_override
    import aws_sdk_mediaconvert.types.hdr10_metadata
    import aws_sdk_mediaconvert.types.input_rotate
    import aws_sdk_mediaconvert.types.input_sample_range
    import aws_sdk_mediaconvert.types.pad_video
    import aws_sdk_mediaconvert.types.video_selector_type


class VideoSelector(TypedDict, closed=True):
    alpha_behavior: NotRequired[
        "aws_sdk_mediaconvert.types.alpha_behavior.AlphaBehavior"
    ]
    """Ignore this setting unless this input is a QuickTime animation with an alpha channel. Use this setting to create separate Key and Fill outputs. In each output, specify which part of the input MediaConvert uses. Leave this setting at the default value DISCARD to delete the alpha channel and preserve the video. Set it to REMAP_TO_LUMA to delete the video and map the alpha channel to the luma channel of your outputs."""
    color_space: NotRequired["aws_sdk_mediaconvert.types.color_space.ColorSpace"]
    """If your input video has accurate color space metadata, or if you don't know about color space: Keep the default value, Follow. MediaConvert will automatically detect your input color space. If your input video has metadata indicating the wrong color space, or has missing metadata: Specify the accurate color space here. If your input video is HDR 10 and the SMPTE ST 2086 Mastering Display Color Volume static metadata isn't present in your video stream, or if that metadata is present but not accurate: Choose Force HDR 10. Specify correct values in the input HDR 10 metadata settings. For more information about HDR jobs, see https://docs.aws.amazon.com/console/mediaconvert/hdr. When you specify an input color space, MediaConvert uses the following color space metadata, which includes color primaries, transfer characteristics, and matrix coefficients: * HDR 10: BT.2020, PQ, BT.2020 non-constant * HLG 2020: BT.2020, HLG, BT.2020 non-constant * P3DCI (Theater): DCIP3, SMPTE 428M, BT.709 * P3D65 (SDR): Display P3, sRGB, BT.709 * P3D65 (HDR): Display P3, PQ, BT.709"""
    color_space_usage: NotRequired[
        "aws_sdk_mediaconvert.types.color_space_usage.ColorSpaceUsage"
    ]
    """There are two sources for color metadata, the input file and the job input settings Color space and HDR master display information settings. The Color space usage setting determines which takes precedence. Choose Force to use color metadata from the input job settings. If you don't specify values for those settings, the service defaults to using metadata from your input. FALLBACK - Choose Fallback to use color metadata from the source when it is present. If there's no color metadata in your input file, the service defaults to using values you specify in the input settings."""
    embedded_timecode_override: NotRequired[
        "aws_sdk_mediaconvert.types.embedded_timecode_override.EmbeddedTimecodeOverride"
    ]
    """Set Embedded timecode override to Use MDPM when your AVCHD input contains timecode tag data in the Modified Digital Video Pack Metadata. When you do, we recommend you also set Timecode source to Embedded. Leave Embedded timecode override blank, or set to None, when your input does not contain MDPM timecode."""
    hdr10_metadata: NotRequired[
        "aws_sdk_mediaconvert.types.hdr10_metadata.Hdr10Metadata"
    ]
    """Use these settings to provide HDR 10 metadata that is missing or inaccurate in your input video. Appropriate values vary depending on the input video and must be provided by a color grader. The color grader generates these values during the HDR 10 mastering process. The valid range for each of these settings is 0 to 50,000. Each increment represents 0.00002 in CIE1931 color coordinate. Related settings - When you specify these values, you must also set Color space to HDR 10. To specify whether the the values you specify here take precedence over the values in the metadata of your input file, set Color space usage. To specify whether color metadata is included in an output, set Color metadata. For more information about MediaConvert HDR jobs, see https://docs.aws.amazon.com/console/mediaconvert/hdr."""
    max_luminance: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the maximum mastering display luminance. Enter an integer from 0 to 2147483647, in units of 0.0001 nits. For example, enter 10000000 for 1000 nits."""
    pad_video: NotRequired["aws_sdk_mediaconvert.types.pad_video.PadVideo"]
    """Use this setting if your input has video and audio durations that don't align, and your output or player has strict alignment requirements. Examples: Input audio track has a delayed start. Input video track ends before audio ends. When you set Pad video to Black, MediaConvert generates black video frames so that output video and audio durations match. Black video frames are added at the beginning or end, depending on your input. To keep the default behavior and not generate black video, set Pad video to Disabled or leave blank."""
    pid: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Use PID to select specific video data from an input file. Specify this value as an integer; the system automatically converts it to the hexidecimal value. For example, 257 selects PID 0x101. A PID, or packet identifier, is an identifier for a set of data in an MPEG-2 transport stream container."""
    program_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Selects a specific program from within a multi-program transport stream. Note that Quad 4K is not currently supported."""
    rotate: NotRequired["aws_sdk_mediaconvert.types.input_rotate.InputRotate"]
    """Use Rotate to specify how the service rotates your video. You can choose automatic rotation or specify a rotation. You can specify a clockwise rotation of 0, 90, 180, or 270 degrees. If your input video container is .mov or .mp4 and your input has rotation metadata, you can choose Automatic to have the service rotate your video according to the rotation specified in the metadata. The rotation must be within one degree of 90, 180, or 270 degrees. If the rotation metadata specifies any other rotation, the service will default to no rotation. By default, the service does no rotation, even if your input video has rotation metadata. The service doesn't pass through rotation metadata."""
    sample_range: NotRequired[
        "aws_sdk_mediaconvert.types.input_sample_range.InputSampleRange"
    ]
    """If the sample range metadata in your input video is accurate, or if you don't know about sample range, keep the default value, Follow, for this setting. When you do, the service automatically detects your input sample range. If your input video has metadata indicating the wrong sample range, specify the accurate sample range here. When you do, MediaConvert ignores any sample range information in the input metadata. Regardless of whether MediaConvert uses the input sample range or the sample range that you specify, MediaConvert uses the sample range for transcoding and also writes it to the output metadata."""
    selector_type: NotRequired[
        "aws_sdk_mediaconvert.types.video_selector_type.VideoSelectorType"
    ]
    """Choose the video selector type for your HLS input. Use to specify which video rendition MediaConvert uses from your HLS input. To have MediaConvert automatically use the highest bitrate rendition from your HLS input: Keep the default value, Auto. To manually specify a rendition: Choose Stream. Then enter the unique stream number in the Streams array, starting at 1, corresponding to the stream order in the manifest."""
    streams: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__integer_min1_max2147483647.__listOf__integerMin1Max2147483647"
    ]
    """Specify one or more video streams for MediaConvert to use from your HLS input. Enter an integer corresponding to the stream number, with the first stream in your HLS multivariant playlist starting at 1. For re-encoding workflows, MediaConvert uses the video stream that you select with the highest bitrate as the input. For video passthrough workflows, you specify whether to passthrough a single video stream or multiple video streams under Video selector source in the output video encoding settings."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelector) -> dict:
    out: dict = {}
    if "alpha_behavior" in value:
        import aws_sdk_mediaconvert.types.alpha_behavior

        out["alphaBehavior"] = aws_sdk_mediaconvert.types.alpha_behavior.serialize_json(
            value["alpha_behavior"]
        )
    if "color_space" in value:
        import aws_sdk_mediaconvert.types.color_space

        out["colorSpace"] = aws_sdk_mediaconvert.types.color_space.serialize_json(
            value["color_space"]
        )
    if "color_space_usage" in value:
        import aws_sdk_mediaconvert.types.color_space_usage

        out["colorSpaceUsage"] = (
            aws_sdk_mediaconvert.types.color_space_usage.serialize_json(
                value["color_space_usage"]
            )
        )
    if "embedded_timecode_override" in value:
        import aws_sdk_mediaconvert.types.embedded_timecode_override

        out["embeddedTimecodeOverride"] = (
            aws_sdk_mediaconvert.types.embedded_timecode_override.serialize_json(
                value["embedded_timecode_override"]
            )
        )
    if "hdr10_metadata" in value:
        import aws_sdk_mediaconvert.types.hdr10_metadata

        out["hdr10Metadata"] = aws_sdk_mediaconvert.types.hdr10_metadata.serialize_json(
            value["hdr10_metadata"]
        )
    if "max_luminance" in value:
        out["maxLuminance"] = value["max_luminance"]
    if "pad_video" in value:
        import aws_sdk_mediaconvert.types.pad_video

        out["padVideo"] = aws_sdk_mediaconvert.types.pad_video.serialize_json(
            value["pad_video"]
        )
    if "pid" in value:
        out["pid"] = value["pid"]
    if "program_number" in value:
        out["programNumber"] = value["program_number"]
    if "rotate" in value:
        import aws_sdk_mediaconvert.types.input_rotate

        out["rotate"] = aws_sdk_mediaconvert.types.input_rotate.serialize_json(
            value["rotate"]
        )
    if "sample_range" in value:
        import aws_sdk_mediaconvert.types.input_sample_range

        out["sampleRange"] = (
            aws_sdk_mediaconvert.types.input_sample_range.serialize_json(
                value["sample_range"]
            )
        )
    if "selector_type" in value:
        import aws_sdk_mediaconvert.types.video_selector_type

        out["selectorType"] = (
            aws_sdk_mediaconvert.types.video_selector_type.serialize_json(
                value["selector_type"]
            )
        )
    if "streams" in value:
        import aws_sdk_mediaconvert.types.__list_of__integer_min1_max2147483647

        out["streams"] = (
            aws_sdk_mediaconvert.types.__list_of__integer_min1_max2147483647.serialize_json(
                value["streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoSelector:
    out: VideoSelector = {}  # type: ignore[typeddict-item]
    if "alphaBehavior" in data:
        import aws_sdk_mediaconvert.types.alpha_behavior

        out["alpha_behavior"] = (
            aws_sdk_mediaconvert.types.alpha_behavior.deserialize_json(
                data["alphaBehavior"]
            )
        )
    if "colorSpace" in data:
        import aws_sdk_mediaconvert.types.color_space

        out["color_space"] = aws_sdk_mediaconvert.types.color_space.deserialize_json(
            data["colorSpace"]
        )
    if "colorSpaceUsage" in data:
        import aws_sdk_mediaconvert.types.color_space_usage

        out["color_space_usage"] = (
            aws_sdk_mediaconvert.types.color_space_usage.deserialize_json(
                data["colorSpaceUsage"]
            )
        )
    if "embeddedTimecodeOverride" in data:
        import aws_sdk_mediaconvert.types.embedded_timecode_override

        out["embedded_timecode_override"] = (
            aws_sdk_mediaconvert.types.embedded_timecode_override.deserialize_json(
                data["embeddedTimecodeOverride"]
            )
        )
    if "hdr10Metadata" in data:
        import aws_sdk_mediaconvert.types.hdr10_metadata

        out["hdr10_metadata"] = (
            aws_sdk_mediaconvert.types.hdr10_metadata.deserialize_json(
                data["hdr10Metadata"]
            )
        )
    if "maxLuminance" in data:
        out["max_luminance"] = data["maxLuminance"]
    if "padVideo" in data:
        import aws_sdk_mediaconvert.types.pad_video

        out["pad_video"] = aws_sdk_mediaconvert.types.pad_video.deserialize_json(
            data["padVideo"]
        )
    if "pid" in data:
        out["pid"] = data["pid"]
    if "programNumber" in data:
        out["program_number"] = data["programNumber"]
    if "rotate" in data:
        import aws_sdk_mediaconvert.types.input_rotate

        out["rotate"] = aws_sdk_mediaconvert.types.input_rotate.deserialize_json(
            data["rotate"]
        )
    if "sampleRange" in data:
        import aws_sdk_mediaconvert.types.input_sample_range

        out["sample_range"] = (
            aws_sdk_mediaconvert.types.input_sample_range.deserialize_json(
                data["sampleRange"]
            )
        )
    if "selectorType" in data:
        import aws_sdk_mediaconvert.types.video_selector_type

        out["selector_type"] = (
            aws_sdk_mediaconvert.types.video_selector_type.deserialize_json(
                data["selectorType"]
            )
        )
    if "streams" in data:
        import aws_sdk_mediaconvert.types.__list_of__integer_min1_max2147483647

        out["streams"] = (
            aws_sdk_mediaconvert.types.__list_of__integer_min1_max2147483647.deserialize_json(
                data["streams"]
            )
        )
    return out
