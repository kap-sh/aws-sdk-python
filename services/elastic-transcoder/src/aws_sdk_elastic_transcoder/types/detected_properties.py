"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#DetectedProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.float_string
    import aws_sdk_elastic_transcoder.types.nullable_integer
    import aws_sdk_elastic_transcoder.types.nullable_long


class DetectedProperties(TypedDict):
    width: NotRequired[
        "aws_sdk_elastic_transcoder.types.nullable_integer.NullableInteger"
    ]
    """<p>The detected width of the input file, in pixels.</p>"""
    height: NotRequired[
        "aws_sdk_elastic_transcoder.types.nullable_integer.NullableInteger"
    ]
    """<p>The detected height of the input file, in pixels.</p>"""
    frame_rate: NotRequired["aws_sdk_elastic_transcoder.types.float_string.FloatString"]
    """<p>The detected frame rate of the input file, in frames per second.</p>"""
    file_size: NotRequired[
        "aws_sdk_elastic_transcoder.types.nullable_long.NullableLong"
    ]
    """<p>The detected file size of the input file, in bytes.</p>"""
    duration_millis: NotRequired[
        "aws_sdk_elastic_transcoder.types.nullable_long.NullableLong"
    ]
    """<p>The detected duration of the input file, in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectedProperties) -> dict:
    out: dict = {}
    if "width" in value:
        out["Width"] = value["width"]
    if "height" in value:
        out["Height"] = value["height"]
    if "frame_rate" in value:
        out["FrameRate"] = value["frame_rate"]
    if "file_size" in value:
        out["FileSize"] = value["file_size"]
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    return out


def deserialize_json(data: dict) -> DetectedProperties:
    out: DetectedProperties = {}  # type: ignore[typeddict-item]
    if "Width" in data:
        out["width"] = data["Width"]
    if "Height" in data:
        out["height"] = data["Height"]
    if "FrameRate" in data:
        out["frame_rate"] = data["FrameRate"]
    if "FileSize" in data:
        out["file_size"] = data["FileSize"]
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    return out
