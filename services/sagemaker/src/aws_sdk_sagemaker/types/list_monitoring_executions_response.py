"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMonitoringExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_execution_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListMonitoringExecutionsResponse(TypedDict, closed=True):
    monitoring_execution_summaries: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_execution_summary_list.MonitoringExecutionSummaryList"
    ]
    """<p>A JSON array in which each element is a summary for a monitoring execution.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitoringExecutionsResponse) -> dict:
    out: dict = {}
    if "monitoring_execution_summaries" in value:
        import aws_sdk_sagemaker.types.monitoring_execution_summary_list

        out["MonitoringExecutionSummaries"] = (
            aws_sdk_sagemaker.types.monitoring_execution_summary_list.serialize_aws_json_1_1(
                value["monitoring_execution_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitoringExecutionsResponse:
    out: ListMonitoringExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "MonitoringExecutionSummaries" in data:
        import aws_sdk_sagemaker.types.monitoring_execution_summary_list

        out["monitoring_execution_summaries"] = (
            aws_sdk_sagemaker.types.monitoring_execution_summary_list.deserialize_aws_json_1_1(
                data["MonitoringExecutionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
