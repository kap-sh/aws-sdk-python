"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StartMigrationWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.migration_workflow_status_enum


class StartMigrationWorkflowResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    ]
    """<p>The ID of the migration workflow.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the migration workflow.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
    ]
    """<p>The status of the migration workflow.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the migration workflow.</p>"""
    last_start_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was last started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMigrationWorkflowResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "last_start_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["lastStartTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_start_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartMigrationWorkflowResponse:
    out: StartMigrationWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "lastStartTime" in data:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["last_start_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastStartTime"]
            )
        )
    return out
