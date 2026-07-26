"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeFleetRoleForWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.worker_id


class AssumeFleetRoleForWorkerRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the fleet's farm.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID that contains the worker.</p>"""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The ID of the worker assuming the fleet role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeFleetRoleForWorkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssumeFleetRoleForWorkerRequest:
    out: AssumeFleetRoleForWorkerRequest = {}  # type: ignore[typeddict-item]
    return out
