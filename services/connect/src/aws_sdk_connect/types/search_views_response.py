"""Generated from Smithy shape ``com.amazonaws.connect#SearchViewsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.next_token2500
    import aws_sdk_connect.types.view_search_summary_list


class SearchViewsResponse(TypedDict):
    views: NotRequired[
        "aws_sdk_connect.types.view_search_summary_list.ViewSearchSummaryList"
    ]
    """<p>A list of views that match the search criteria.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The approximate total number of views that match the search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchViewsResponse) -> dict:
    out: dict = {}
    if "views" in value:
        import aws_sdk_connect.types.view_search_summary_list

        out["Views"] = aws_sdk_connect.types.view_search_summary_list.serialize_json(
            value["views"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchViewsResponse:
    out: SearchViewsResponse = {}  # type: ignore[typeddict-item]
    if "Views" in data:
        import aws_sdk_connect.types.view_search_summary_list

        out["views"] = aws_sdk_connect.types.view_search_summary_list.deserialize_json(
            data["Views"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
