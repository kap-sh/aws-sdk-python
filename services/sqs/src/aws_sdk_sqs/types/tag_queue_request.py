"""Generated from Smithy shape ``com.amazonaws.sqs#TagQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string
    import aws_sdk_sqs.types.tag_map


class TagQueueRequest(TypedDict, closed=True):
    queue_url: "aws_sdk_sqs.types.string.String"
    """<p>The URL of the queue.</p>"""
    tags: "aws_sdk_sqs.types.tag_map.TagMap"
    """<p>The list of tags to be added to the specified queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagQueueRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    import aws_sdk_sqs.types.tag_map

    out["Tags"] = aws_sdk_sqs.types.tag_map.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagQueueRequest:
    out: TagQueueRequest = {}  # type: ignore[typeddict-item]
    if "QueueUrl" in data:
        out["queue_url"] = data["QueueUrl"]
    else:
        raise DeserializationError("TagQueueRequest.queue_url required")
    if "Tags" in data:
        import aws_sdk_sqs.types.tag_map

        out["tags"] = aws_sdk_sqs.types.tag_map.deserialize_aws_json_1_0(data["Tags"])
    else:
        raise DeserializationError("TagQueueRequest.tags required")
    return out
