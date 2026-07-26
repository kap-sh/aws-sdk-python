"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.worker_id


class BatchGetWorkerIdentifier(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the worker.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the worker.</p>"""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The worker ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    return out


def deserialize_json(data: dict) -> BatchGetWorkerIdentifier:
    out: BatchGetWorkerIdentifier = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetWorkerIdentifier.farm_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("BatchGetWorkerIdentifier.fleet_id required")
    if "workerId" in data:
        out["worker_id"] = data["workerId"]
    else:
        raise DeserializationError("BatchGetWorkerIdentifier.worker_id required")
    return out
