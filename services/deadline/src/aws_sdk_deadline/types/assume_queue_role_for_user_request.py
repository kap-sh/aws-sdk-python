"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.queue_id


class AssumeQueueRoleForUserRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the queue that the user assumes the role for.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the queue that the user assumes the role for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForUserRequest:
    out: AssumeQueueRoleForUserRequest = {}  # type: ignore[typeddict-item]
    return out
