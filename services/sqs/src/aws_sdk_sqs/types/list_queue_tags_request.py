"""Generated from Smithy shape ``com.amazonaws.sqs#ListQueueTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string


class ListQueueTagsRequest(TypedDict, closed=True):
    queue_url: "aws_sdk_sqs.types.string.String"
    """<p>The URL of the queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListQueueTagsRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListQueueTagsRequest:
    out: ListQueueTagsRequest = {}  # type: ignore[typeddict-item]
    if "QueueUrl" in data:
        out["queue_url"] = data["QueueUrl"]
    else:
        raise DeserializationError("ListQueueTagsRequest.queue_url required")
    return out
