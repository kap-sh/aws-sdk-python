"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListDashboardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.dashboard_name
    import aws_sdk_cloudtrail.types.dashboard_type
    import aws_sdk_cloudtrail.types.list_dashboards_max_results_count
    import aws_sdk_cloudtrail.types.pagination_token


class ListDashboardsRequest(TypedDict, closed=True):
    name_prefix: NotRequired["aws_sdk_cloudtrail.types.dashboard_name.DashboardName"]
    """<p> Specify a name prefix to filter on. </p>"""
    type: NotRequired["aws_sdk_cloudtrail.types.dashboard_type.DashboardType"]
    """<p> Specify a dashboard type to filter on: <code>CUSTOM</code> or <code>MANAGED</code>. </p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p> A token you can use to get the next page of dashboard results. </p>"""
    max_results: NotRequired[
        "aws_sdk_cloudtrail.types.list_dashboards_max_results_count.ListDashboardsMaxResultsCount"
    ]
    """<p> The maximum number of dashboards to display on a single page. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDashboardsRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "type" in value:
        import aws_sdk_cloudtrail.types.dashboard_type

        out["Type"] = aws_sdk_cloudtrail.types.dashboard_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDashboardsRequest:
    out: ListDashboardsRequest = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "Type" in data:
        import aws_sdk_cloudtrail.types.dashboard_type

        out["type"] = aws_sdk_cloudtrail.types.dashboard_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
