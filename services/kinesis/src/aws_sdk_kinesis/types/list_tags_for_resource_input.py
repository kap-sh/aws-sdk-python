"""Generated from Smithy shape ``com.amazonaws.kinesis#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.resource_arn
    import aws_sdk_kinesis.types.stream_id


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_kinesis.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the Kinesis resource for which to list tags.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceInput.resource_arn required")
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
