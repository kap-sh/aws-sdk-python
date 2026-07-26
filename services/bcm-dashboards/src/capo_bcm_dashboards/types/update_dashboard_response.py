"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#UpdateDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn


class UpdateDashboardResponse(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the updated dashboard.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDashboardResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDashboardResponse:
    out: UpdateDashboardResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateDashboardResponse.arn required")
    return out
