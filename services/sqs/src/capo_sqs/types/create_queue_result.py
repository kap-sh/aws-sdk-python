"""Generated from Smithy shape ``com.amazonaws.sqs#CreateQueueResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class CreateQueueResult(TypedDict, closed=True):
    queue_url: NotRequired["capo_sqs.types.string.String"]
    """<p>The URL of the created Amazon SQS queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateQueueResult) -> dict:
    out: dict = {}
    if "queue_url" in value:
        out["QueueUrl"] = value["queue_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateQueueResult:
    out: CreateQueueResult = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    return out
