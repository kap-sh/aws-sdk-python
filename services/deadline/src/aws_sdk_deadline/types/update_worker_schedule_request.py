"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateWorkerScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.updated_session_actions
    import aws_sdk_deadline.types.worker_id


class UpdateWorkerScheduleRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID to update.</p>"""
    worker_id: "aws_sdk_deadline.types.worker_id.WorkerId"
    """<p>The worker ID to update.</p>"""
    updated_session_actions: NotRequired[
        "aws_sdk_deadline.types.updated_session_actions.UpdatedSessionActions"
    ]
    """<p>The session actions associated with the worker schedule to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkerScheduleRequest) -> dict:
    out: dict = {}
    if "updated_session_actions" in value:
        import aws_sdk_deadline.types.updated_session_actions

        out["updatedSessionActions"] = (
            aws_sdk_deadline.types.updated_session_actions.serialize_json(
                value["updated_session_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkerScheduleRequest:
    out: UpdateWorkerScheduleRequest = {}  # type: ignore[typeddict-item]
    if "updatedSessionActions" in data:
        import aws_sdk_deadline.types.updated_session_actions

        out["updated_session_actions"] = (
            aws_sdk_deadline.types.updated_session_actions.deserialize_json(
                data["updatedSessionActions"]
            )
        )
    return out
