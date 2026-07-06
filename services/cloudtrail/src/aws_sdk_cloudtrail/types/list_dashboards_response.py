"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListDashboardsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.dashboards
    import aws_sdk_cloudtrail.types.pagination_token


class ListDashboardsResponse(TypedDict, closed=True):
    dashboards: NotRequired["aws_sdk_cloudtrail.types.dashboards.Dashboards"]
    """<p> Contains information about dashboards in the account, in the current Region that match the applied filters. </p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p> A token you can use to get the next page of dashboard results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDashboardsResponse) -> dict:
    out: dict = {}
    if "dashboards" in value:
        import aws_sdk_cloudtrail.types.dashboards

        out["Dashboards"] = aws_sdk_cloudtrail.types.dashboards.serialize_aws_json_1_1(
            value["dashboards"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDashboardsResponse:
    out: ListDashboardsResponse = {}  # type: ignore[typeddict-item]
    if "Dashboards" in data:
        import aws_sdk_cloudtrail.types.dashboards

        out["dashboards"] = (
            aws_sdk_cloudtrail.types.dashboards.deserialize_aws_json_1_1(
                data["Dashboards"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
