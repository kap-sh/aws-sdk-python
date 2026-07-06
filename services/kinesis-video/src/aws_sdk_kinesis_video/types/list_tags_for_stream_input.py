"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListTagsForStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.next_token
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name


class ListTagsForStreamInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_kinesis_video.types.next_token.NextToken"]
    """<p>If you specify this parameter and the result of a <code>ListTagsForStream</code> call is truncated, the response includes a token that you can use in the next request to fetch the next batch of tags.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream that you want to list tags for.</p>"""
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream that you want to list tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForStreamInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    return out


def deserialize_json(data: dict) -> ListTagsForStreamInput:
    out: ListTagsForStreamInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    return out
