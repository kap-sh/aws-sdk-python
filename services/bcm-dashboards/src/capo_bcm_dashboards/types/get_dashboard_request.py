"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GetDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn


class GetDashboardRequest(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard to retrieve. This is required to uniquely identify the dashboard.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDashboardRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDashboardRequest:
    out: GetDashboardRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetDashboardRequest.arn required")
    return out
