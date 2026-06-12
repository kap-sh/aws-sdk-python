"""Generated from Smithy shape ``com.amazonaws.connect#ListViewsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.views_next_token
    import aws_sdk_connect.types.views_summary_list


class ListViewsResponse(TypedDict):
    views_summary_list: NotRequired[
        "aws_sdk_connect.types.views_summary_list.ViewsSummaryList"
    ]
    """<p>A list of view summaries.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.views_next_token.ViewsNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListViewsResponse) -> dict:
    out: dict = {}
    if "views_summary_list" in value:
        import aws_sdk_connect.types.views_summary_list

        out["ViewsSummaryList"] = (
            aws_sdk_connect.types.views_summary_list.serialize_json(
                value["views_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListViewsResponse:
    out: ListViewsResponse = {}  # type: ignore[typeddict-item]
    if "ViewsSummaryList" in data:
        import aws_sdk_connect.types.views_summary_list

        out["views_summary_list"] = (
            aws_sdk_connect.types.views_summary_list.deserialize_json(
                data["ViewsSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
