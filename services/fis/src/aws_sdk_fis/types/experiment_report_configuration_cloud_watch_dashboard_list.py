"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportConfigurationCloudWatchDashboardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard

ExperimentReportConfigurationCloudWatchDashboardList: TypeAlias = list[
    "aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard.ExperimentReportConfigurationCloudWatchDashboard"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportConfigurationCloudWatchDashboardList) -> list:
    import aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> ExperimentReportConfigurationCloudWatchDashboardList:
    import aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard

    out: ExperimentReportConfigurationCloudWatchDashboardList = []
    for item in data:
        out.append(
            aws_sdk_fis.types.experiment_report_configuration_cloud_watch_dashboard.deserialize_json(
                item
            )
        )
    return out
