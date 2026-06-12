"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#SqsQueueConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.sqs_queue_policy


class SqsQueueConfiguration(TypedDict):
    queue_policy: NotRequired[
        "aws_sdk_accessanalyzer.types.sqs_queue_policy.SqsQueuePolicy"
    ]
    """<p> The proposed resource policy for the Amazon SQS queue. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqsQueueConfiguration) -> dict:
    out: dict = {}
    if "queue_policy" in value:
        out["queuePolicy"] = value["queue_policy"]
    return out


def deserialize_json(data: dict) -> SqsQueueConfiguration:
    out: SqsQueueConfiguration = {}  # type: ignore[typeddict-item]
    if "queuePolicy" in data:
        out["queue_policy"] = data["queuePolicy"]
    return out
