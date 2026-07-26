"""Generated from Smithy shape ``com.amazonaws.connect#CreateQueueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.queue_id


class CreateQueueResponse(TypedDict, closed=True):
    queue_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the queue.</p>"""
    queue_id: NotRequired["capo_connect.types.queue_id.QueueId"]
    """<p>The identifier for the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueResponse) -> dict:
    out: dict = {}
    if "queue_arn" in value:
        out["QueueArn"] = value["queue_arn"]
    if "queue_id" in value:
        out["QueueId"] = value["queue_id"]
    return out


def deserialize_json(data: dict) -> CreateQueueResponse:
    out: CreateQueueResponse = {}  # type: ignore[typeddict-item]
    if "QueueArn" in data:
        out["queue_arn"] = data["QueueArn"]
    if "QueueId" in data:
        out["queue_id"] = data["QueueId"]
    return out
