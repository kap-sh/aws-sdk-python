"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMonitoringAlertsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.monitoring_schedule_name
    import capo_sagemaker.types.next_token


class ListMonitoringAlertsRequest(TypedDict, closed=True):
    monitoring_schedule_name: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of a monitoring schedule.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListMonitoringAlerts</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of alerts in the history, use the token in the next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to display. The default is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitoringAlertsRequest) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitoringAlertsRequest:
    out: ListMonitoringAlertsRequest = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
