"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StopMigrationWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum


class StopMigrationWorkflowResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    ]
    """<p>The ID of the migration workflow.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the migration workflow.</p>"""
    status: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
    ]
    """<p>The status of the migration workflow.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the migration workflow.</p>"""
    last_stop_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopMigrationWorkflowResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "last_stop_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["lastStopTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_stop_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> StopMigrationWorkflowResponse:
    out: StopMigrationWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "lastStopTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["last_stop_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastStopTime"]
            )
        )
    return out
