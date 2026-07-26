"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateReportConfigurationCloudWatchDashboardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_report_configuration_cloud_watch_dashboard

ExperimentTemplateReportConfigurationCloudWatchDashboardList: TypeAlias = list[
    "capo_fis.types.experiment_template_report_configuration_cloud_watch_dashboard.ExperimentTemplateReportConfigurationCloudWatchDashboard"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: ExperimentTemplateReportConfigurationCloudWatchDashboardList,
) -> list:
    import capo_fis.types.experiment_template_report_configuration_cloud_watch_dashboard

    out: list = []
    for item in value:
        out.append(
            capo_fis.types.experiment_template_report_configuration_cloud_watch_dashboard.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> ExperimentTemplateReportConfigurationCloudWatchDashboardList:
    import capo_fis.types.experiment_template_report_configuration_cloud_watch_dashboard

    out: ExperimentTemplateReportConfigurationCloudWatchDashboardList = []
    for item in data:
        out.append(
            capo_fis.types.experiment_template_report_configuration_cloud_watch_dashboard.deserialize_json(
                item
            )
        )
    return out
