"""Generated from Smithy shape ``com.amazonaws.kinesis#ListTagsForStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.list_tags_for_stream_input_limit
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.stream_name
    import aws_sdk_kinesis.types.tag_key


class ListTagsForStreamInput(TypedDict, closed=True):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    exclusive_start_tag_key: NotRequired["aws_sdk_kinesis.types.tag_key.TagKey"]
    """<p>The key to use as the starting point for the list of tags. If this parameter is set, <code>ListTagsForStream</code> gets all tags that occur after <code>ExclusiveStartTagKey</code>. </p>"""
    limit: NotRequired[
        "aws_sdk_kinesis.types.list_tags_for_stream_input_limit.ListTagsForStreamInputLimit"
    ]
    """<p>The number of tags to return. If this number is less than the total number of tags associated with the stream, <code>HasMoreTags</code> is set to <code>true</code>. To list additional tags, set <code>ExclusiveStartTagKey</code> to the last key in the response.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForStreamInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "exclusive_start_tag_key" in value:
        out["ExclusiveStartTagKey"] = value["exclusive_start_tag_key"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForStreamInput:
    out: ListTagsForStreamInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "ExclusiveStartTagKey" in data:
        out["exclusive_start_tag_key"] = data["ExclusiveStartTagKey"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
