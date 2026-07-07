"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#DeleteMigrationWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id


class DeleteMigrationWorkflowRequest(TypedDict, closed=True):
    id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMigrationWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMigrationWorkflowRequest:
    out: DeleteMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
