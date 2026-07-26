"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeImageGenerationConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name


class DescribeImageGenerationConfigurationInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream from which to retrieve the image generation configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>. </p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the Kinesis video stream from which to retrieve the image generation configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeImageGenerationConfigurationInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    return out


def deserialize_json(data: dict) -> DescribeImageGenerationConfigurationInput:
    out: DescribeImageGenerationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    return out
