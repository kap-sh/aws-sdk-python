"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.client_token
    import capo_migrationhuborchestrator.types.template_id


class UpdateTemplateRequest(TypedDict, closed=True):
    id: "capo_migrationhuborchestrator.types.template_id.TemplateId"
    """<p>The ID of the request to update a migration workflow template.</p>"""
    template_name: NotRequired["str"]
    """<p>The name of the migration workflow template to update.</p>"""
    template_description: NotRequired["str"]
    """<p>The description of the migration workflow template to update.</p>"""
    client_token: NotRequired[
        "capo_migrationhuborchestrator.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateRequest) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "template_description" in value:
        out["templateDescription"] = value["template_description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateTemplateRequest:
    out: UpdateTemplateRequest = {}  # type: ignore[typeddict-item]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    if "templateDescription" in data:
        out["template_description"] = data["templateDescription"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
