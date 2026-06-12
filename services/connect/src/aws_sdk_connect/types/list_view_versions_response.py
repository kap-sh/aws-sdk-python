"""Generated from Smithy shape ``com.amazonaws.connect#ListViewVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.view_version_summary_list
    import aws_sdk_connect.types.views_next_token


class ListViewVersionsResponse(TypedDict):
    view_version_summary_list: NotRequired[
        "aws_sdk_connect.types.view_version_summary_list.ViewVersionSummaryList"
    ]
    """<p>A list of view version summaries.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.views_next_token.ViewsNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListViewVersionsResponse) -> dict:
    out: dict = {}
    if "view_version_summary_list" in value:
        import aws_sdk_connect.types.view_version_summary_list

        out["ViewVersionSummaryList"] = (
            aws_sdk_connect.types.view_version_summary_list.serialize_json(
                value["view_version_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListViewVersionsResponse:
    out: ListViewVersionsResponse = {}  # type: ignore[typeddict-item]
    if "ViewVersionSummaryList" in data:
        import aws_sdk_connect.types.view_version_summary_list

        out["view_version_summary_list"] = (
            aws_sdk_connect.types.view_version_summary_list.deserialize_json(
                data["ViewVersionSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
