"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DeleteDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.dashboard_arn


class DeleteDashboardRequest(TypedDict, closed=True):
    arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDashboardRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDashboardRequest:
    out: DeleteDashboardRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteDashboardRequest.arn required")
    return out
