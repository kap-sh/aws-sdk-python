"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTemplateAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.template_alias


class UpdateTemplateAliasResponse(TypedDict, closed=True):
    template_alias: NotRequired["capo_quicksight.types.template_alias.TemplateAlias"]
    """<p>The template alias.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateAliasResponse) -> dict:
    out: dict = {}
    if "template_alias" in value:
        import capo_quicksight.types.template_alias

        out["TemplateAlias"] = capo_quicksight.types.template_alias.serialize_json(
            value["template_alias"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateTemplateAliasResponse:
    out: UpdateTemplateAliasResponse = {}  # type: ignore[typeddict-item]
    if "TemplateAlias" in data:
        import capo_quicksight.types.template_alias

        out["template_alias"] = capo_quicksight.types.template_alias.deserialize_json(
            data["TemplateAlias"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
