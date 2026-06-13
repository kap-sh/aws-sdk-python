"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTemplateVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.template_version_summary_list


class ListTemplateVersionsResponse(TypedDict):
    template_version_summary_list: NotRequired[
        "aws_sdk_quicksight.types.template_version_summary_list.TemplateVersionSummaryList"
    ]
    """<p>A structure containing a list of all the versions of the specified template.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateVersionsResponse) -> dict:
    out: dict = {}
    if "template_version_summary_list" in value:
        import aws_sdk_quicksight.types.template_version_summary_list

        out["TemplateVersionSummaryList"] = (
            aws_sdk_quicksight.types.template_version_summary_list.serialize_json(
                value["template_version_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListTemplateVersionsResponse:
    out: ListTemplateVersionsResponse = {}  # type: ignore[typeddict-item]
    if "TemplateVersionSummaryList" in data:
        import aws_sdk_quicksight.types.template_version_summary_list

        out["template_version_summary_list"] = (
            aws_sdk_quicksight.types.template_version_summary_list.deserialize_json(
                data["TemplateVersionSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
