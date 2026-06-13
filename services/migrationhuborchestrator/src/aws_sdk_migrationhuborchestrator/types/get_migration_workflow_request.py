"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetMigrationWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id


class GetMigrationWorkflowRequest(TypedDict):
    id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMigrationWorkflowRequest:
    out: GetMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
