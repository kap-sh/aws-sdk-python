"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#DeleteTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.template_id


class DeleteTemplateRequest(TypedDict):
    id: "aws_sdk_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the request to delete a migration workflow template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTemplateRequest:
    out: DeleteTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
