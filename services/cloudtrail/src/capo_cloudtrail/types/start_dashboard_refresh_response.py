"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartDashboardRefreshResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.refresh_id


class StartDashboardRefreshResponse(TypedDict, closed=True):
    refresh_id: NotRequired["capo_cloudtrail.types.refresh_id.RefreshId"]
    """<p> The refresh ID for the dashboard. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDashboardRefreshResponse) -> dict:
    out: dict = {}
    if "refresh_id" in value:
        out["RefreshId"] = value["refresh_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDashboardRefreshResponse:
    out: StartDashboardRefreshResponse = {}  # type: ignore[typeddict-item]
    if "RefreshId" in data:
        out["refresh_id"] = data["RefreshId"]
    return out
