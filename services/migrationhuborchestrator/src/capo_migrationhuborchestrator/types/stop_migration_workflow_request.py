"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StopMigrationWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_id


class StopMigrationWorkflowRequest(TypedDict, closed=True):
    id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopMigrationWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopMigrationWorkflowRequest:
    out: StopMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
