"""Generated from Smithy shape ``com.amazonaws.fis#ReportConfigurationCloudWatchDashboardInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input

ReportConfigurationCloudWatchDashboardInputList: TypeAlias = list[
    "aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input.ReportConfigurationCloudWatchDashboardInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportConfigurationCloudWatchDashboardInputList) -> list:
    import aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReportConfigurationCloudWatchDashboardInputList:
    import aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input

    out: ReportConfigurationCloudWatchDashboardInputList = []
    for item in data:
        out.append(
            aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input.deserialize_json(
                item
            )
        )
    return out
