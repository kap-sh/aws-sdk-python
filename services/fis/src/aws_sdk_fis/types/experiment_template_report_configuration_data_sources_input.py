"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateReportConfigurationDataSourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input_list


class ExperimentTemplateReportConfigurationDataSourcesInput(TypedDict, closed=True):
    cloud_watch_dashboards: NotRequired[
        "aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input_list.ReportConfigurationCloudWatchDashboardInputList"
    ]
    """<p>The CloudWatch dashboards to include as data sources in the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ExperimentTemplateReportConfigurationDataSourcesInput,
) -> dict:
    out: dict = {}
    if "cloud_watch_dashboards" in value:
        import aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input_list

        out["cloudWatchDashboards"] = (
            aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input_list.serialize_json(
                value["cloud_watch_dashboards"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> ExperimentTemplateReportConfigurationDataSourcesInput:
    out: ExperimentTemplateReportConfigurationDataSourcesInput = {}  # type: ignore[typeddict-item]
    if "cloudWatchDashboards" in data:
        import aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input_list

        out["cloud_watch_dashboards"] = (
            aws_sdk_fis.types.report_configuration_cloud_watch_dashboard_input_list.deserialize_json(
                data["cloudWatchDashboards"]
            )
        )
    return out
