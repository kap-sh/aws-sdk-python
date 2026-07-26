"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeQueueRoleForWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.worker_id


class AssumeQueueRoleForWorkerRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the worker assuming the queue role.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the worker assuming the queue role.</p>"""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The worker ID of the worker assuming the queue role.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the worker assuming the queue role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeQueueRoleForWorkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssumeQueueRoleForWorkerRequest:
    out: AssumeQueueRoleForWorkerRequest = {}  # type: ignore[typeddict-item]
    return out
