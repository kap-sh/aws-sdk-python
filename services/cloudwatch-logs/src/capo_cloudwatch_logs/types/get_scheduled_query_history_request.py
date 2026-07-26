"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetScheduledQueryHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.execution_status_list
    import capo_cloudwatch_logs.types.get_scheduled_query_history_max_results
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.scheduled_query_identifier
    import capo_cloudwatch_logs.types.timestamp


class GetScheduledQueryHistoryRequest(TypedDict, closed=True):
    identifier: (
        "capo_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier"
    )
    """<p>The ARN or name of the scheduled query to retrieve history for.</p>"""
    start_time: "capo_cloudwatch_logs.types.timestamp.Timestamp"
    """<p>The start time for the history query in Unix epoch format.</p>"""
    end_time: "capo_cloudwatch_logs.types.timestamp.Timestamp"
    """<p>The end time for the history query in Unix epoch format.</p>"""
    execution_statuses: NotRequired[
        "capo_cloudwatch_logs.types.execution_status_list.ExecutionStatusList"
    ]
    """<p>An array of execution statuses to filter the history results. Only executions with the specified statuses are returned.</p>"""
    max_results: NotRequired[
        "capo_cloudwatch_logs.types.get_scheduled_query_history_max_results.GetScheduledQueryHistoryMaxResults"
    ]
    """<p>The maximum number of history records to return. Valid range is 1 to 1000.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScheduledQueryHistoryRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["startTime"] = value["start_time"]
    out["endTime"] = value["end_time"]
    if "execution_statuses" in value:
        import capo_cloudwatch_logs.types.execution_status_list

        out["executionStatuses"] = (
            capo_cloudwatch_logs.types.execution_status_list.serialize_aws_json_1_1(
                value["execution_statuses"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScheduledQueryHistoryRequest:
    out: GetScheduledQueryHistoryRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError(
            "GetScheduledQueryHistoryRequest.identifier required"
        )
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    else:
        raise DeserializationError(
            "GetScheduledQueryHistoryRequest.start_time required"
        )
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    else:
        raise DeserializationError("GetScheduledQueryHistoryRequest.end_time required")
    if "executionStatuses" in data:
        import capo_cloudwatch_logs.types.execution_status_list

        out["execution_statuses"] = (
            capo_cloudwatch_logs.types.execution_status_list.deserialize_aws_json_1_1(
                data["executionStatuses"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
