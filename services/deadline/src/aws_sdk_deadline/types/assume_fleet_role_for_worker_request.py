"""Generated from Smithy shape ``com.amazonaws.deadline#AssumeFleetRoleForWorkerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.worker_id


class AssumeFleetRoleForWorkerRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the fleet's farm.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID that contains the worker.</p>"""
    worker_id: "aws_sdk_deadline.types.worker_id.WorkerId"
    """<p>The ID of the worker assuming the fleet role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeFleetRoleForWorkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssumeFleetRoleForWorkerRequest:
    out: AssumeFleetRoleForWorkerRequest = {}  # type: ignore[typeddict-item]
    return out
