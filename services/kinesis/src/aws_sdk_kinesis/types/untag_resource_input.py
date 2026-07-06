"""Generated from Smithy shape ``com.amazonaws.kinesis#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.resource_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    tag_keys: "aws_sdk_kinesis.types.tag_key_list.TagKeyList"
    """<p>A list of tag key-value pairs. Existing tags of the resource whose keys are members of this list will be removed from the Kinesis resource.</p>"""
    resource_arn: "aws_sdk_kinesis.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the Kinesis resource from which to remove tags.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_kinesis.types.tag_key_list

    out["TagKeys"] = aws_sdk_kinesis.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    out["ResourceARN"] = value["resource_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "TagKeys" in data:
        import aws_sdk_kinesis.types.tag_key_list

        out["tag_keys"] = aws_sdk_kinesis.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
