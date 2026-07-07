"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ListDashboardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.max_results
    import aws_sdk_bcm_dashboards.types.next_page_token


class ListDashboardsRequest(TypedDict, closed=True):
    max_results: "aws_sdk_bcm_dashboards.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. The default value is 20.</p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_dashboards.types.next_page_token.NextPageToken"
    ]
    """<p>The token for the next page of results. Use the value returned in the previous response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDashboardsRequest) -> dict:
    out: dict = {}
    out["maxResults"] = value.get("max_results", 20)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDashboardsRequest:
    out: ListDashboardsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 20
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
