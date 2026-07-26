"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#CreateDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn


class CreateDashboardResponse(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the newly created dashboard.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDashboardResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDashboardResponse:
    out: CreateDashboardResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateDashboardResponse.arn required")
    return out
