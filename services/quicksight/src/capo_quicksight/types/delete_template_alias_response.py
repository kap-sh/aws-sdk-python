"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteTemplateAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DeleteTemplateAliasResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    template_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>An ID for the template associated with the deletion.</p>"""
    alias_name: NotRequired["capo_quicksight.types.alias_name.AliasName"]
    """<p>The name for the template alias.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the template you want to delete.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTemplateAliasResponse) -> dict:
    out: dict = {}
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteTemplateAliasResponse:
    out: DeleteTemplateAliasResponse = {}  # type: ignore[typeddict-item]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
