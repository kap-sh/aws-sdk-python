"""Generated from Smithy shape ``com.amazonaws.rekognition#VideoMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.float
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.u_long
    import aws_sdk_rekognition.types.video_color_range


class VideoMetadata(TypedDict, closed=True):
    codec: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Type of compression used in the analyzed video. </p>"""
    duration_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>Length of the video in milliseconds.</p>"""
    format: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Format of the analyzed video. Possible values are MP4, MOV and AVI. </p>"""
    frame_rate: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>Number of frames per second in the video.</p>"""
    frame_height: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>Vertical pixel dimension of the video.</p>"""
    frame_width: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>Horizontal pixel dimension of the video.</p>"""
    color_range: NotRequired[
        "aws_sdk_rekognition.types.video_color_range.VideoColorRange"
    ]
    """<p> A description of the range of luminance values in a video, either LIMITED (16 to 235) or FULL (0 to 255). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VideoMetadata) -> dict:
    out: dict = {}
    if "codec" in value:
        out["Codec"] = value["codec"]
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    if "format" in value:
        out["Format"] = value["format"]
    if "frame_rate" in value:
        out["FrameRate"] = value["frame_rate"]
    if "frame_height" in value:
        out["FrameHeight"] = value["frame_height"]
    if "frame_width" in value:
        out["FrameWidth"] = value["frame_width"]
    if "color_range" in value:
        import aws_sdk_rekognition.types.video_color_range

        out["ColorRange"] = (
            aws_sdk_rekognition.types.video_color_range.serialize_aws_json_1_1(
                value["color_range"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VideoMetadata:
    out: VideoMetadata = {}  # type: ignore[typeddict-item]
    if "Codec" in data:
        out["codec"] = data["Codec"]
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    if "Format" in data:
        out["format"] = data["Format"]
    if "FrameRate" in data:
        out["frame_rate"] = data["FrameRate"]
    if "FrameHeight" in data:
        out["frame_height"] = data["FrameHeight"]
    if "FrameWidth" in data:
        out["frame_width"] = data["FrameWidth"]
    if "ColorRange" in data:
        import aws_sdk_rekognition.types.video_color_range

        out["color_range"] = (
            aws_sdk_rekognition.types.video_color_range.deserialize_aws_json_1_1(
                data["ColorRange"]
            )
        )
    return out
