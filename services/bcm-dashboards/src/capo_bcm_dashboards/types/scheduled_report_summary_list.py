"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ScheduledReportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.scheduled_report_summary

ScheduledReportSummaryList: TypeAlias = list[
    "capo_bcm_dashboards.types.scheduled_report_summary.ScheduledReportSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledReportSummaryList) -> list:
    import capo_bcm_dashboards.types.scheduled_report_summary

    out: list = []
    for item in value:
        out.append(
            capo_bcm_dashboards.types.scheduled_report_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ScheduledReportSummaryList:
    import capo_bcm_dashboards.types.scheduled_report_summary

    out: ScheduledReportSummaryList = []
    for item in data:
        out.append(
            capo_bcm_dashboards.types.scheduled_report_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
