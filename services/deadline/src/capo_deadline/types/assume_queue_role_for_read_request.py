"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForReadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.queue_id


class AssumeQueueRoleForReadRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm containing the queue.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForReadRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForReadRequest:
    out: AssumeQueueRoleForReadRequest = {}  # type: ignore[typeddict-item]
    return out
