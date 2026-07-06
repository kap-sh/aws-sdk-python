"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.dashboard_arn


class GetDashboardRequest(TypedDict, closed=True):
    dashboard_id: "aws_sdk_cloudtrail.types.dashboard_arn.DashboardArn"
    """<p> The name or ARN for the dashboard. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDashboardRequest) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDashboardRequest:
    out: GetDashboardRequest = {}  # type: ignore[typeddict-item]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    else:
        raise DeserializationError("GetDashboardRequest.dashboard_id required")
    return out
