"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StartMigrationWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_id


class StartMigrationWorkflowRequest(TypedDict, closed=True):
    id: "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMigrationWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartMigrationWorkflowRequest:
    out: StartMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
