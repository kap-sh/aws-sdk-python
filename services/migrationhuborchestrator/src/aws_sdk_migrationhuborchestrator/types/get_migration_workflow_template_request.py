"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetMigrationWorkflowTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.template_id


class GetMigrationWorkflowTemplateRequest(TypedDict):
    id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationWorkflowTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMigrationWorkflowTemplateRequest:
    out: GetMigrationWorkflowTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
