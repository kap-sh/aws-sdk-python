"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.template_summary_list


class ListTemplatesResponse(TypedDict, closed=True):
    template_summary_list: NotRequired[
        "aws_sdk_quicksight.types.template_summary_list.TemplateSummaryList"
    ]
    """<p>A structure containing information about the templates in the list.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplatesResponse) -> dict:
    out: dict = {}
    if "template_summary_list" in value:
        import aws_sdk_quicksight.types.template_summary_list

        out["TemplateSummaryList"] = (
            aws_sdk_quicksight.types.template_summary_list.serialize_json(
                value["template_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListTemplatesResponse:
    out: ListTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "TemplateSummaryList" in data:
        import aws_sdk_quicksight.types.template_summary_list

        out["template_summary_list"] = (
            aws_sdk_quicksight.types.template_summary_list.deserialize_json(
                data["TemplateSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
