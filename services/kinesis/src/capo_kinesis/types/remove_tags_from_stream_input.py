"""Generated from Smithy shape ``com.amazonaws.kinesis#RemoveTagsFromStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.tag_key_list


class RemoveTagsFromStreamInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    tag_keys: "capo_kinesis.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys. Each corresponding tag is removed from the stream.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromStreamInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import capo_kinesis.types.tag_key_list

    out["TagKeys"] = capo_kinesis.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromStreamInput:
    out: RemoveTagsFromStreamInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "TagKeys" in data:
        import capo_kinesis.types.tag_key_list

        out["tag_keys"] = capo_kinesis.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("RemoveTagsFromStreamInput.tag_keys required")
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
