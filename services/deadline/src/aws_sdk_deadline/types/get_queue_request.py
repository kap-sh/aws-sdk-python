"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.queue_id


class GetQueueRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm in the queue.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the queue to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueRequest:
    out: GetQueueRequest = {}  # type: ignore[typeddict-item]
    return out
