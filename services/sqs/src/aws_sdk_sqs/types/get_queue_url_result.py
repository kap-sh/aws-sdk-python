"""Generated from Smithy shape ``com.amazonaws.sqs#GetQueueUrlResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string


class GetQueueUrlResult(TypedDict):
    queue_url: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>The URL of the queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQueueUrlResult) -> dict:
    out: dict = {}
    if "queue_url" in value:
        out["QueueUrl"] = value["queue_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQueueUrlResult:
    out: GetQueueUrlResult = {}  # type: ignore[typeddict-item]
    if "QueueUrl" in data:
        out["queue_url"] = data["QueueUrl"]
    return out
