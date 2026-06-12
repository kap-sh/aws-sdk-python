"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateReportConfigurationCloudWatchDashboard``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_identifier


class ExperimentTemplateReportConfigurationCloudWatchDashboard(TypedDict):
    dashboard_identifier: NotRequired[
        "aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_identifier.ReportConfigurationCloudWatchDashboardIdentifier"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch dashboard to include in the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ExperimentTemplateReportConfigurationCloudWatchDashboard,
) -> dict:
    out: dict = {}
    if "dashboard_identifier" in value:
        out["dashboardIdentifier"] = value["dashboard_identifier"]
    return out


def deserialize_json(
    data: dict,
) -> ExperimentTemplateReportConfigurationCloudWatchDashboard:
    out: ExperimentTemplateReportConfigurationCloudWatchDashboard = {}  # type: ignore[typeddict-item]
    if "dashboardIdentifier" in data:
        out["dashboard_identifier"] = data["dashboardIdentifier"]
    return out
