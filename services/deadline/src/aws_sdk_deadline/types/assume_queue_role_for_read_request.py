"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForReadRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.queue_id


class AssumeQueueRoleForReadRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm containing the queue.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForReadRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForReadRequest:
    out: AssumeQueueRoleForReadRequest = {}  # type: ignore[typeddict-item]
    return out
