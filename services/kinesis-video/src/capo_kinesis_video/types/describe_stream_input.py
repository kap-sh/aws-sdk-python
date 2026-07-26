"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name


class DescribeStreamInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStreamInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    return out


def deserialize_json(data: dict) -> DescribeStreamInput:
    out: DescribeStreamInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    return out
