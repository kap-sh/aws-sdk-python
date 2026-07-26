"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetMigrationWorkflowTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.template_id


class GetMigrationWorkflowTemplateRequest(TypedDict, closed=True):
    id: "capo_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationWorkflowTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMigrationWorkflowTemplateRequest:
    out: GetMigrationWorkflowTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
