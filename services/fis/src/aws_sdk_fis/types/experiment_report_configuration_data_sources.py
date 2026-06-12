"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportConfigurationDataSources``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard_list


class ExperimentReportConfigurationDataSources(TypedDict):
    cloud_watch_dashboards: NotRequired[
        "aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard_list.ExperimentReportConfigurationCloudWatchDashboardList"
    ]
    """<p>The CloudWatch dashboards to include as data sources in the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportConfigurationDataSources) -> dict:
    out: dict = {}
    if "cloud_watch_dashboards" in value:
        import aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard_list

        out["cloudWatchDashboards"] = (
            aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard_list.serialize_json(
                value["cloud_watch_dashboards"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentReportConfigurationDataSources:
    out: ExperimentReportConfigurationDataSources = {}  # type: ignore[typeddict-item]
    if "cloudWatchDashboards" in data:
        import aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard_list

        out["cloud_watch_dashboards"] = (
            aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard_list.deserialize_json(
                data["cloudWatchDashboards"]
            )
        )
    return out
