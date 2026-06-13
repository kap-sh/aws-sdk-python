"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StopMigrationWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id


class StopMigrationWorkflowRequest(TypedDict):
    id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopMigrationWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopMigrationWorkflowRequest:
    out: StopMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
