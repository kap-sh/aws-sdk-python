"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max15
    import aws_sdk_mediaconvert.types.__integer_min0_max100
    import aws_sdk_mediaconvert.types.__integer_min32_max8192
    import aws_sdk_mediaconvert.types.afd_signaling
    import aws_sdk_mediaconvert.types.anti_alias
    import aws_sdk_mediaconvert.types.chroma_position_mode
    import aws_sdk_mediaconvert.types.color_metadata
    import aws_sdk_mediaconvert.types.drop_frame_timecode
    import aws_sdk_mediaconvert.types.rectangle
    import aws_sdk_mediaconvert.types.respond_to_afd
    import aws_sdk_mediaconvert.types.scaling_behavior
    import aws_sdk_mediaconvert.types.timecode_track
    import aws_sdk_mediaconvert.types.video_codec_settings
    import aws_sdk_mediaconvert.types.video_preprocessor
    import aws_sdk_mediaconvert.types.video_timecode_insertion


class VideoDescription(TypedDict):
    afd_signaling: NotRequired["aws_sdk_mediaconvert.types.afd_signaling.AfdSignaling"]
    """This setting only applies to H.264, H.265, and MPEG2 outputs. Use Insert AFD signaling to specify whether the service includes AFD values in the output video data and what those values are. * Choose None to remove all AFD values from this output. * Choose Fixed to ignore input AFD values and instead encode the value specified in the job. * Choose Auto to calculate output AFD values based on the input AFD scaler data."""
    anti_alias: NotRequired["aws_sdk_mediaconvert.types.anti_alias.AntiAlias"]
    """The anti-alias filter is automatically applied to all outputs. The service no longer accepts the value DISABLED for AntiAlias. If you specify that in your job, the service will ignore the setting."""
    chroma_position_mode: NotRequired[
        "aws_sdk_mediaconvert.types.chroma_position_mode.ChromaPositionMode"
    ]
    """Specify the chroma sample positioning metadata for your H.264 or H.265 output. To have MediaConvert automatically determine chroma positioning: We recommend that you keep the default value, Auto. To specify center positioning: Choose Force center. To specify top left positioning: Choose Force top left."""
    codec_settings: NotRequired[
        "aws_sdk_mediaconvert.types.video_codec_settings.VideoCodecSettings"
    ]
    """Video codec settings contains the group of settings related to video encoding. The settings in this group vary depending on the value that you choose for Video codec. For each codec enum that you choose, define the corresponding settings object. The following lists the codec enum, settings object pairs. * AV1, Av1Settings * AVC_INTRA, AvcIntraSettings * FRAME_CAPTURE, FrameCaptureSettings * GIF, GifSettings * H_264, H264Settings * H_265, H265Settings * MPEG2, Mpeg2Settings * PRORES, ProresSettings * UNCOMPRESSED, UncompressedSettings * VC3, Vc3Settings * VP8, Vp8Settings * VP9, Vp9Settings * XAVC, XavcSettings"""
    color_metadata: NotRequired[
        "aws_sdk_mediaconvert.types.color_metadata.ColorMetadata"
    ]
    """Choose Insert for this setting to include color metadata in this output. Choose Ignore to exclude color metadata from this output. If you don't specify a value, the service sets this to Insert by default."""
    crop: NotRequired["aws_sdk_mediaconvert.types.rectangle.Rectangle"]
    """Use Cropping selection to specify the video area that the service will include in the output video frame."""
    drop_frame_timecode: NotRequired[
        "aws_sdk_mediaconvert.types.drop_frame_timecode.DropFrameTimecode"
    ]
    """Applies only to 29.97 fps outputs. When this feature is enabled, the service will use drop-frame timecode on outputs. If it is not possible to use drop-frame timecode, the system will fall back to non-drop-frame. This setting is enabled by default when Timecode insertion or Timecode track is enabled."""
    fixed_afd: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max15.__integerMin0Max15"
    ]
    """Applies only if you set AFD Signaling to Fixed. Use Fixed to specify a four-bit AFD value which the service will write on all frames of this video output."""
    height: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8192.__integerMin32Max8192"
    ]
    """Use Height to define the video resolution height, in pixels, for this output. To use the same resolution as your input: Leave both Width and Height blank. To evenly scale from your input resolution: Leave Height blank and enter a value for Width. For example, if your input is 1920x1080 and you set Width to 1280, your output will be 1280x720."""
    position: NotRequired["aws_sdk_mediaconvert.types.rectangle.Rectangle"]
    """Use Selection placement to define the video area in your output frame. The area outside of the rectangle that you specify here is black."""
    respond_to_afd: NotRequired[
        "aws_sdk_mediaconvert.types.respond_to_afd.RespondToAfd"
    ]
    """Use Respond to AFD to specify how the service changes the video itself in response to AFD values in the input. * Choose Respond to clip the input video frame according to the AFD value, input display aspect ratio, and output display aspect ratio. * Choose Passthrough to include the input AFD values. Do not choose this when AfdSignaling is set to NONE. A preferred implementation of this workflow is to set RespondToAfd to and set AfdSignaling to AUTO. * Choose None to remove all input AFD values from this output."""
    scaling_behavior: NotRequired[
        "aws_sdk_mediaconvert.types.scaling_behavior.ScalingBehavior"
    ]
    """Specify the video Scaling behavior when your output has a different resolution than your input. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/video-scaling.html Select Smart Cropping using Elemental Inference as your scaling behavior to have Elemental Inference automatically crop your video. Smart Crop requires a vertical output aspect ratio (1:1 is the widest aspect ratio supported)."""
    sharpness: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Use Sharpness setting to specify the strength of anti-aliasing. This setting changes the width of the anti-alias filter kernel used for scaling. Sharpness only applies if your output resolution is different from your input resolution. 0 is the softest setting, 100 the sharpest, and 50 recommended for most content."""
    timecode_insertion: NotRequired[
        "aws_sdk_mediaconvert.types.video_timecode_insertion.VideoTimecodeInsertion"
    ]
    """Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input frame rate is identical to the output frame rate. To include timecodes in this output, set Timecode insertion to PIC_TIMING_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration. In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration does."""
    timecode_track: NotRequired[
        "aws_sdk_mediaconvert.types.timecode_track.TimecodeTrack"
    ]
    """To include a timecode track in your MP4 output: Choose Enabled. MediaConvert writes the timecode track in the Null Media Header box (NMHD), without any timecode text formatting information. You can also specify dropframe or non-dropframe timecode under the Drop Frame Timecode setting. To not include a timecode track: Keep the default value, Disabled."""
    video_preprocessors: NotRequired[
        "aws_sdk_mediaconvert.types.video_preprocessor.VideoPreprocessor"
    ]
    """Find additional transcoding features under Preprocessors. Enable the features at each output individually. These features are disabled by default."""
    width: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8192.__integerMin32Max8192"
    ]
    """Use Width to define the video resolution width, in pixels, for this output. To use the same resolution as your input: Leave both Width and Height blank. To evenly scale from your input resolution: Leave Width blank and enter a value for Height. For example, if your input is 1920x1080 and you set Height to 720, your output will be 1280x720."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoDescription) -> dict:
    out: dict = {}
    if "afd_signaling" in value:
        import aws_sdk_mediaconvert.types.afd_signaling

        out["afdSignaling"] = aws_sdk_mediaconvert.types.afd_signaling.serialize_json(
            value["afd_signaling"]
        )
    if "anti_alias" in value:
        import aws_sdk_mediaconvert.types.anti_alias

        out["antiAlias"] = aws_sdk_mediaconvert.types.anti_alias.serialize_json(
            value["anti_alias"]
        )
    if "chroma_position_mode" in value:
        import aws_sdk_mediaconvert.types.chroma_position_mode

        out["chromaPositionMode"] = (
            aws_sdk_mediaconvert.types.chroma_position_mode.serialize_json(
                value["chroma_position_mode"]
            )
        )
    if "codec_settings" in value:
        import aws_sdk_mediaconvert.types.video_codec_settings

        out["codecSettings"] = (
            aws_sdk_mediaconvert.types.video_codec_settings.serialize_json(
                value["codec_settings"]
            )
        )
    if "color_metadata" in value:
        import aws_sdk_mediaconvert.types.color_metadata

        out["colorMetadata"] = aws_sdk_mediaconvert.types.color_metadata.serialize_json(
            value["color_metadata"]
        )
    if "crop" in value:
        import aws_sdk_mediaconvert.types.rectangle

        out["crop"] = aws_sdk_mediaconvert.types.rectangle.serialize_json(value["crop"])
    if "drop_frame_timecode" in value:
        import aws_sdk_mediaconvert.types.drop_frame_timecode

        out["dropFrameTimecode"] = (
            aws_sdk_mediaconvert.types.drop_frame_timecode.serialize_json(
                value["drop_frame_timecode"]
            )
        )
    if "fixed_afd" in value:
        out["fixedAfd"] = value["fixed_afd"]
    if "height" in value:
        out["height"] = value["height"]
    if "position" in value:
        import aws_sdk_mediaconvert.types.rectangle

        out["position"] = aws_sdk_mediaconvert.types.rectangle.serialize_json(
            value["position"]
        )
    if "respond_to_afd" in value:
        import aws_sdk_mediaconvert.types.respond_to_afd

        out["respondToAfd"] = aws_sdk_mediaconvert.types.respond_to_afd.serialize_json(
            value["respond_to_afd"]
        )
    if "scaling_behavior" in value:
        import aws_sdk_mediaconvert.types.scaling_behavior

        out["scalingBehavior"] = (
            aws_sdk_mediaconvert.types.scaling_behavior.serialize_json(
                value["scaling_behavior"]
            )
        )
    if "sharpness" in value:
        out["sharpness"] = value["sharpness"]
    if "timecode_insertion" in value:
        import aws_sdk_mediaconvert.types.video_timecode_insertion

        out["timecodeInsertion"] = (
            aws_sdk_mediaconvert.types.video_timecode_insertion.serialize_json(
                value["timecode_insertion"]
            )
        )
    if "timecode_track" in value:
        import aws_sdk_mediaconvert.types.timecode_track

        out["timecodeTrack"] = aws_sdk_mediaconvert.types.timecode_track.serialize_json(
            value["timecode_track"]
        )
    if "video_preprocessors" in value:
        import aws_sdk_mediaconvert.types.video_preprocessor

        out["videoPreprocessors"] = (
            aws_sdk_mediaconvert.types.video_preprocessor.serialize_json(
                value["video_preprocessors"]
            )
        )
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> VideoDescription:
    out: VideoDescription = {}  # type: ignore[typeddict-item]
    if "afdSignaling" in data:
        import aws_sdk_mediaconvert.types.afd_signaling

        out["afd_signaling"] = (
            aws_sdk_mediaconvert.types.afd_signaling.deserialize_json(
                data["afdSignaling"]
            )
        )
    if "antiAlias" in data:
        import aws_sdk_mediaconvert.types.anti_alias

        out["anti_alias"] = aws_sdk_mediaconvert.types.anti_alias.deserialize_json(
            data["antiAlias"]
        )
    if "chromaPositionMode" in data:
        import aws_sdk_mediaconvert.types.chroma_position_mode

        out["chroma_position_mode"] = (
            aws_sdk_mediaconvert.types.chroma_position_mode.deserialize_json(
                data["chromaPositionMode"]
            )
        )
    if "codecSettings" in data:
        import aws_sdk_mediaconvert.types.video_codec_settings

        out["codec_settings"] = (
            aws_sdk_mediaconvert.types.video_codec_settings.deserialize_json(
                data["codecSettings"]
            )
        )
    if "colorMetadata" in data:
        import aws_sdk_mediaconvert.types.color_metadata

        out["color_metadata"] = (
            aws_sdk_mediaconvert.types.color_metadata.deserialize_json(
                data["colorMetadata"]
            )
        )
    if "crop" in data:
        import aws_sdk_mediaconvert.types.rectangle

        out["crop"] = aws_sdk_mediaconvert.types.rectangle.deserialize_json(
            data["crop"]
        )
    if "dropFrameTimecode" in data:
        import aws_sdk_mediaconvert.types.drop_frame_timecode

        out["drop_frame_timecode"] = (
            aws_sdk_mediaconvert.types.drop_frame_timecode.deserialize_json(
                data["dropFrameTimecode"]
            )
        )
    if "fixedAfd" in data:
        out["fixed_afd"] = data["fixedAfd"]
    if "height" in data:
        out["height"] = data["height"]
    if "position" in data:
        import aws_sdk_mediaconvert.types.rectangle

        out["position"] = aws_sdk_mediaconvert.types.rectangle.deserialize_json(
            data["position"]
        )
    if "respondToAfd" in data:
        import aws_sdk_mediaconvert.types.respond_to_afd

        out["respond_to_afd"] = (
            aws_sdk_mediaconvert.types.respond_to_afd.deserialize_json(
                data["respondToAfd"]
            )
        )
    if "scalingBehavior" in data:
        import aws_sdk_mediaconvert.types.scaling_behavior

        out["scaling_behavior"] = (
            aws_sdk_mediaconvert.types.scaling_behavior.deserialize_json(
                data["scalingBehavior"]
            )
        )
    if "sharpness" in data:
        out["sharpness"] = data["sharpness"]
    if "timecodeInsertion" in data:
        import aws_sdk_mediaconvert.types.video_timecode_insertion

        out["timecode_insertion"] = (
            aws_sdk_mediaconvert.types.video_timecode_insertion.deserialize_json(
                data["timecodeInsertion"]
            )
        )
    if "timecodeTrack" in data:
        import aws_sdk_mediaconvert.types.timecode_track

        out["timecode_track"] = (
            aws_sdk_mediaconvert.types.timecode_track.deserialize_json(
                data["timecodeTrack"]
            )
        )
    if "videoPreprocessors" in data:
        import aws_sdk_mediaconvert.types.video_preprocessor

        out["video_preprocessors"] = (
            aws_sdk_mediaconvert.types.video_preprocessor.deserialize_json(
                data["videoPreprocessors"]
            )
        )
    if "width" in data:
        out["width"] = data["width"]
    return out
