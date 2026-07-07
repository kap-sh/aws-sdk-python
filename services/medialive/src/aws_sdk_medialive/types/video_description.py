"""Generated from Smithy shape ``com.amazonaws.medialive#VideoDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__integer_min0_max100
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.video_codec_settings
    import aws_sdk_medialive.types.video_description_respond_to_afd
    import aws_sdk_medialive.types.video_description_scaling_behavior


class VideoDescription(TypedDict, closed=True):
    codec_settings: NotRequired[
        "aws_sdk_medialive.types.video_codec_settings.VideoCodecSettings"
    ]
    """Video codec settings."""
    height: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """Output video height, in pixels. Must be an even number. For most codecs, you can leave this field and width blank in order to use the height and width (resolution) from the source. Note, however, that leaving blank is not recommended. For the Frame Capture codec, height and width are required."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of this VideoDescription. Outputs will use this name to uniquely identify this Description. Description names should be unique within this Live Event."""
    respond_to_afd: NotRequired[
        "aws_sdk_medialive.types.video_description_respond_to_afd.VideoDescriptionRespondToAfd"
    ]
    """Indicates how MediaLive will respond to the AFD values that might be in the input video. If you do not know what AFD signaling is, or if your downstream system has not given you guidance, choose PASSTHROUGH. RESPOND: MediaLive clips the input video using a formula that uses the AFD values (configured in afdSignaling ), the input display aspect ratio, and the output display aspect ratio. MediaLive also includes the AFD values in the output, unless the codec for this encode is FRAME_CAPTURE. PASSTHROUGH: MediaLive ignores the AFD values and does not clip the video. But MediaLive does include the values in the output. NONE: MediaLive does not clip the input video and does not include the AFD values in the output"""
    scaling_behavior: NotRequired[
        "aws_sdk_medialive.types.video_description_scaling_behavior.VideoDescriptionScalingBehavior"
    ]
    """Configures how MediaLive transforms the video picture to match the output frame. Use STRETCH_TO_OUTPUT to stretch the video to fill the output frame. The video might get distorted. Use DEFAULT to insert pillar boxes or letter boxes around the video to fill the output frame. The video won't get distorted. Use SMART_CROP to enable the smart crop feature that uses the Elemental Inference service to crop the frame using AI - see the MediaLive User Guide for more information."""
    sharpness: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Changes the strength of the anti-alias filter used for scaling. 0 is the softest setting, 100 is the sharpest. A setting of 50 is recommended for most content."""
    width: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """Output video width, in pixels. Must be an even number. For most codecs, you can leave this field and height blank in order to use the height and width (resolution) from the source. Note, however, that leaving blank is not recommended. For the Frame Capture codec, height and width are required."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoDescription) -> dict:
    out: dict = {}
    if "codec_settings" in value:
        import aws_sdk_medialive.types.video_codec_settings

        out["codecSettings"] = (
            aws_sdk_medialive.types.video_codec_settings.serialize_json(
                value["codec_settings"]
            )
        )
    if "height" in value:
        out["height"] = value["height"]
    if "name" in value:
        out["name"] = value["name"]
    if "respond_to_afd" in value:
        import aws_sdk_medialive.types.video_description_respond_to_afd

        out["respondToAfd"] = (
            aws_sdk_medialive.types.video_description_respond_to_afd.serialize_json(
                value["respond_to_afd"]
            )
        )
    if "scaling_behavior" in value:
        import aws_sdk_medialive.types.video_description_scaling_behavior

        out["scalingBehavior"] = (
            aws_sdk_medialive.types.video_description_scaling_behavior.serialize_json(
                value["scaling_behavior"]
            )
        )
    if "sharpness" in value:
        out["sharpness"] = value["sharpness"]
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> VideoDescription:
    out: VideoDescription = {}  # type: ignore[typeddict-item]
    if "codecSettings" in data:
        import aws_sdk_medialive.types.video_codec_settings

        out["codec_settings"] = (
            aws_sdk_medialive.types.video_codec_settings.deserialize_json(
                data["codecSettings"]
            )
        )
    if "height" in data:
        out["height"] = data["height"]
    if "name" in data:
        out["name"] = data["name"]
    if "respondToAfd" in data:
        import aws_sdk_medialive.types.video_description_respond_to_afd

        out["respond_to_afd"] = (
            aws_sdk_medialive.types.video_description_respond_to_afd.deserialize_json(
                data["respondToAfd"]
            )
        )
    if "scalingBehavior" in data:
        import aws_sdk_medialive.types.video_description_scaling_behavior

        out["scaling_behavior"] = (
            aws_sdk_medialive.types.video_description_scaling_behavior.deserialize_json(
                data["scalingBehavior"]
            )
        )
    if "sharpness" in data:
        out["sharpness"] = data["sharpness"]
    if "width" in data:
        out["width"] = data["width"]
    return out
