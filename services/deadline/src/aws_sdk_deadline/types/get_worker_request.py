"""Generated from Smithy shape ``com.amazonaws.deadline#GetWorkerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.worker_id


class GetWorkerRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the worker.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the worker.</p>"""
    worker_id: "aws_sdk_deadline.types.worker_id.WorkerId"
    """<p>The worker ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkerRequest:
    out: GetWorkerRequest = {}  # type: ignore[typeddict-item]
    return out
