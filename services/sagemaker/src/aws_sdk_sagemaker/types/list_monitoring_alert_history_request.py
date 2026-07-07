"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMonitoringAlertHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.monitoring_alert_history_sort_key
    import aws_sdk_sagemaker.types.monitoring_alert_name
    import aws_sdk_sagemaker.types.monitoring_alert_status
    import aws_sdk_sagemaker.types.monitoring_schedule_name
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListMonitoringAlertHistoryRequest(TypedDict, closed=True):
    monitoring_schedule_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of a monitoring schedule.</p>"""
    monitoring_alert_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_name.MonitoringAlertName"
    ]
    """<p>The name of a monitoring alert.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_history_sort_key.MonitoringAlertHistorySortKey"
    ]
    """<p>The field used to sort results. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order, whether <code>Ascending</code> or <code>Descending</code>, of the alert history. The default is <code>Descending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListMonitoringAlertHistory</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of alerts in the history, use the token in the next request.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to display. The default is 100.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only alerts created on or before the specified time.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only alerts created on or after the specified time.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_status.MonitoringAlertStatus"
    ]
    """<p>A filter that retrieves only alerts with a specific status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitoringAlertHistoryRequest) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_alert_name" in value:
        out["MonitoringAlertName"] = value["monitoring_alert_name"]
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.monitoring_alert_history_sort_key

        out["SortBy"] = (
            aws_sdk_sagemaker.types.monitoring_alert_history_sort_key.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.monitoring_alert_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.monitoring_alert_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitoringAlertHistoryRequest:
    out: ListMonitoringAlertHistoryRequest = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if "MonitoringAlertName" in data:
        out["monitoring_alert_name"] = data["MonitoringAlertName"]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.monitoring_alert_history_sort_key

        out["sort_by"] = (
            aws_sdk_sagemaker.types.monitoring_alert_history_sort_key.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.monitoring_alert_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.monitoring_alert_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    return out
