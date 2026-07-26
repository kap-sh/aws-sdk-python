"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#SqsQueueConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.sqs_queue_policy


class SqsQueueConfiguration(TypedDict, closed=True):
    queue_policy: NotRequired[
        "capo_accessanalyzer.types.sqs_queue_policy.SqsQueuePolicy"
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
