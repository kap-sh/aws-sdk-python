"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportConfigurationDataSources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_report_configuration_cloud_watch_dashboard_list


class ExperimentReportConfigurationDataSources(TypedDict, closed=True):
    cloud_watch_dashboards: NotRequired[
        "capo_fis.types.experiment_report_configuration_cloud_watch_dashboard_list.ExperimentReportConfigurationCloudWatchDashboardList"
    ]
    """<p>The CloudWatch dashboards to include as data sources in the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportConfigurationDataSources) -> dict:
    out: dict = {}
    if "cloud_watch_dashboards" in value:
        import capo_fis.types.experiment_report_configuration_cloud_watch_dashboard_list

        out["cloudWatchDashboards"] = (
            capo_fis.types.experiment_report_configuration_cloud_watch_dashboard_list.serialize_json(
                value["cloud_watch_dashboards"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentReportConfigurationDataSources:
    out: ExperimentReportConfigurationDataSources = {}  # type: ignore[typeddict-item]
    if "cloudWatchDashboards" in data:
        import capo_fis.types.experiment_report_configuration_cloud_watch_dashboard_list

        out["cloud_watch_dashboards"] = (
            capo_fis.types.experiment_report_configuration_cloud_watch_dashboard_list.deserialize_json(
                data["cloudWatchDashboards"]
            )
        )
    return out
