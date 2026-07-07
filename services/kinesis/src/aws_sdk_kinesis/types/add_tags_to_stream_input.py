"""Generated from Smithy shape ``com.amazonaws.kinesis#AddTagsToStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.stream_name
    import aws_sdk_kinesis.types.tag_map


class AddTagsToStreamInput(TypedDict, closed=True):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    tags: "aws_sdk_kinesis.types.tag_map.TagMap"
    """<p>A set of up to 50 key-value pairs to use to create the tags. A tag consists of a required key and an optional value. You can add up to 50 tags per resource.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToStreamInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import aws_sdk_kinesis.types.tag_map

    out["Tags"] = aws_sdk_kinesis.types.tag_map.serialize_aws_json_1_1(value["tags"])
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToStreamInput:
    out: AddTagsToStreamInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "Tags" in data:
        import aws_sdk_kinesis.types.tag_map

        out["tags"] = aws_sdk_kinesis.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("AddTagsToStreamInput.tags required")
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
