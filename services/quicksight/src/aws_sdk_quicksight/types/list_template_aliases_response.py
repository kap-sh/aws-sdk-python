"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTemplateAliasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.template_alias_list


class ListTemplateAliasesResponse(TypedDict):
    template_alias_list: NotRequired[
        "aws_sdk_quicksight.types.template_alias_list.TemplateAliasList"
    ]
    """<p>A structure containing the list of the template's aliases.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateAliasesResponse) -> dict:
    out: dict = {}
    if "template_alias_list" in value:
        import aws_sdk_quicksight.types.template_alias_list

        out["TemplateAliasList"] = (
            aws_sdk_quicksight.types.template_alias_list.serialize_json(
                value["template_alias_list"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTemplateAliasesResponse:
    out: ListTemplateAliasesResponse = {}  # type: ignore[typeddict-item]
    if "TemplateAliasList" in data:
        import aws_sdk_quicksight.types.template_alias_list

        out["template_alias_list"] = (
            aws_sdk_quicksight.types.template_alias_list.deserialize_json(
                data["TemplateAliasList"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
