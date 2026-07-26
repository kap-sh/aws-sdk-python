"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TriggerHistoryRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.execution_status
    import capo_cloudwatch_logs.types.query_id
    import capo_cloudwatch_logs.types.scheduled_query_destination_list
    import capo_cloudwatch_logs.types.string
    import capo_cloudwatch_logs.types.timestamp


class TriggerHistoryRecord(TypedDict, closed=True):
    query_id: NotRequired["capo_cloudwatch_logs.types.query_id.QueryId"]
    """<p>The unique identifier for this query execution.</p>"""
    execution_status: NotRequired[
        "capo_cloudwatch_logs.types.execution_status.ExecutionStatus"
    ]
    """<p>The execution status of the scheduled query run.</p>"""
    triggered_timestamp: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the scheduled query execution was triggered.</p>"""
    error_message: NotRequired["capo_cloudwatch_logs.types.string.String"]
    """<p>Error message if the query execution failed.</p>"""
    destinations: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_destination_list.ScheduledQueryDestinationList"
    ]
    """<p>Information about destination processing for this query execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerHistoryRecord) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["queryId"] = value["query_id"]
    if "execution_status" in value:
        import capo_cloudwatch_logs.types.execution_status

        out["executionStatus"] = (
            capo_cloudwatch_logs.types.execution_status.serialize_aws_json_1_1(
                value["execution_status"]
            )
        )
    if "triggered_timestamp" in value:
        out["triggeredTimestamp"] = value["triggered_timestamp"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "destinations" in value:
        import capo_cloudwatch_logs.types.scheduled_query_destination_list

        out["destinations"] = (
            capo_cloudwatch_logs.types.scheduled_query_destination_list.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TriggerHistoryRecord:
    out: TriggerHistoryRecord = {}  # type: ignore[typeddict-item]
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    if "executionStatus" in data:
        import capo_cloudwatch_logs.types.execution_status

        out["execution_status"] = (
            capo_cloudwatch_logs.types.execution_status.deserialize_aws_json_1_1(
                data["executionStatus"]
            )
        )
    if "triggeredTimestamp" in data:
        out["triggered_timestamp"] = data["triggeredTimestamp"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "destinations" in data:
        import capo_cloudwatch_logs.types.scheduled_query_destination_list

        out["destinations"] = (
            capo_cloudwatch_logs.types.scheduled_query_destination_list.deserialize_aws_json_1_1(
                data["destinations"]
            )
        )
    return out
