"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CloudWatchDashboard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.cloud_watch_dashboard_name


class CloudWatchDashboard(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_service_catalog.types.cloud_watch_dashboard_name.CloudWatchDashboardName"
    ]
    """<p>The name of the CloudWatch dashboard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchDashboard) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchDashboard:
    out: CloudWatchDashboard = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
