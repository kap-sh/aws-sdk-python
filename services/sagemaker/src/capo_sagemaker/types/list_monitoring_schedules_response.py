"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMonitoringSchedulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_schedule_summary_list
    import capo_sagemaker.types.next_token


class ListMonitoringSchedulesResponse(TypedDict, closed=True):
    monitoring_schedule_summaries: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_summary_list.MonitoringScheduleSummaryList"
    ]
    """<p>A JSON array in which each element is a summary for a monitoring schedule.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitoringSchedulesResponse) -> dict:
    out: dict = {}
    if "monitoring_schedule_summaries" in value:
        import capo_sagemaker.types.monitoring_schedule_summary_list

        out["MonitoringScheduleSummaries"] = (
            capo_sagemaker.types.monitoring_schedule_summary_list.serialize_aws_json_1_1(
                value["monitoring_schedule_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitoringSchedulesResponse:
    out: ListMonitoringSchedulesResponse = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleSummaries" in data:
        import capo_sagemaker.types.monitoring_schedule_summary_list

        out["monitoring_schedule_summaries"] = (
            capo_sagemaker.types.monitoring_schedule_summary_list.deserialize_aws_json_1_1(
                data["MonitoringScheduleSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
