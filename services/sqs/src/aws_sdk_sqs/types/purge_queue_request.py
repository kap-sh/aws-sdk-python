"""Generated from Smithy shape ``com.amazonaws.sqs#PurgeQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string


class PurgeQueueRequest(TypedDict):
    queue_url: "aws_sdk_sqs.types.string.String"
    """<p>The URL of the queue from which the <code>PurgeQueue</code> action deletes messages.</p> <p>Queue URLs and names are case-sensitive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurgeQueueRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PurgeQueueRequest:
    out: PurgeQueueRequest = {}  # type: ignore[typeddict-item]
    if "QueueUrl" in data:
        out["queue_url"] = data["QueueUrl"]
    else:
        raise DeserializationError("PurgeQueueRequest.queue_url required")
    return out
