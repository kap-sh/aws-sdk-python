"""Generated from Smithy shape ``com.amazonaws.fis#ReportConfigurationCloudWatchDashboardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.report_configuration_cloud_watch_dashboard_identifier


class ReportConfigurationCloudWatchDashboardInput(TypedDict, closed=True):
    dashboard_identifier: NotRequired[
        "capo_fis.types.report_configuration_cloud_watch_dashboard_identifier.ReportConfigurationCloudWatchDashboardIdentifier"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch dashboard to include in the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportConfigurationCloudWatchDashboardInput) -> dict:
    out: dict = {}
    if "dashboard_identifier" in value:
        out["dashboardIdentifier"] = value["dashboard_identifier"]
    return out


def deserialize_json(data: dict) -> ReportConfigurationCloudWatchDashboardInput:
    out: ReportConfigurationCloudWatchDashboardInput = {}  # type: ignore[typeddict-item]
    if "dashboardIdentifier" in data:
        out["dashboard_identifier"] = data["dashboardIdentifier"]
    return out
