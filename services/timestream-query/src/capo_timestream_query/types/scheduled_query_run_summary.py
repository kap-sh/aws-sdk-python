"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQueryRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.error_message
    import capo_timestream_query.types.error_report_location
    import capo_timestream_query.types.execution_stats
    import capo_timestream_query.types.scheduled_query_insights_response
    import capo_timestream_query.types.scheduled_query_run_status
    import capo_timestream_query.types.time


class ScheduledQueryRunSummary(TypedDict, closed=True):
    invocation_time: NotRequired["capo_timestream_query.types.time.Time"]
    """<p>InvocationTime for this run. This is the time at which the query is scheduled to run. Parameter <code>@scheduled_runtime</code> can be used in the query to get the value. </p>"""
    trigger_time: NotRequired["capo_timestream_query.types.time.Time"]
    """<p>The actual time when the query was run.</p>"""
    run_status: NotRequired[
        "capo_timestream_query.types.scheduled_query_run_status.ScheduledQueryRunStatus"
    ]
    """<p>The status of a scheduled query run.</p>"""
    execution_stats: NotRequired[
        "capo_timestream_query.types.execution_stats.ExecutionStats"
    ]
    """<p>Runtime statistics for a scheduled run.</p>"""
    query_insights_response: NotRequired[
        "capo_timestream_query.types.scheduled_query_insights_response.ScheduledQueryInsightsResponse"
    ]
    """<p>Provides various insights and metrics related to the run summary of the scheduled query.</p>"""
    error_report_location: NotRequired[
        "capo_timestream_query.types.error_report_location.ErrorReportLocation"
    ]
    """<p>S3 location for error report.</p>"""
    failure_reason: NotRequired[
        "capo_timestream_query.types.error_message.ErrorMessage"
    ]
    """<p>Error message for the scheduled query in case of failure. You might have to look at the error report to get more detailed error reasons. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQueryRunSummary) -> dict:
    out: dict = {}
    if "invocation_time" in value:
        import capo_timestream_query.types.time

        out["InvocationTime"] = capo_timestream_query.types.time.serialize_aws_json_1_0(
            value["invocation_time"]
        )
    if "trigger_time" in value:
        import capo_timestream_query.types.time

        out["TriggerTime"] = capo_timestream_query.types.time.serialize_aws_json_1_0(
            value["trigger_time"]
        )
    if "run_status" in value:
        import capo_timestream_query.types.scheduled_query_run_status

        out["RunStatus"] = (
            capo_timestream_query.types.scheduled_query_run_status.serialize_aws_json_1_0(
                value["run_status"]
            )
        )
    if "execution_stats" in value:
        import capo_timestream_query.types.execution_stats

        out["ExecutionStats"] = (
            capo_timestream_query.types.execution_stats.serialize_aws_json_1_0(
                value["execution_stats"]
            )
        )
    if "query_insights_response" in value:
        import capo_timestream_query.types.scheduled_query_insights_response

        out["QueryInsightsResponse"] = (
            capo_timestream_query.types.scheduled_query_insights_response.serialize_aws_json_1_0(
                value["query_insights_response"]
            )
        )
    if "error_report_location" in value:
        import capo_timestream_query.types.error_report_location

        out["ErrorReportLocation"] = (
            capo_timestream_query.types.error_report_location.serialize_aws_json_1_0(
                value["error_report_location"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledQueryRunSummary:
    out: ScheduledQueryRunSummary = {}  # type: ignore[typeddict-item]
    if "InvocationTime" in data:
        import capo_timestream_query.types.time

        out["invocation_time"] = (
            capo_timestream_query.types.time.deserialize_aws_json_1_0(
                data["InvocationTime"]
            )
        )
    if "TriggerTime" in data:
        import capo_timestream_query.types.time

        out["trigger_time"] = capo_timestream_query.types.time.deserialize_aws_json_1_0(
            data["TriggerTime"]
        )
    if "RunStatus" in data:
        import capo_timestream_query.types.scheduled_query_run_status

        out["run_status"] = (
            capo_timestream_query.types.scheduled_query_run_status.deserialize_aws_json_1_0(
                data["RunStatus"]
            )
        )
    if "ExecutionStats" in data:
        import capo_timestream_query.types.execution_stats

        out["execution_stats"] = (
            capo_timestream_query.types.execution_stats.deserialize_aws_json_1_0(
                data["ExecutionStats"]
            )
        )
    if "QueryInsightsResponse" in data:
        import capo_timestream_query.types.scheduled_query_insights_response

        out["query_insights_response"] = (
            capo_timestream_query.types.scheduled_query_insights_response.deserialize_aws_json_1_0(
                data["QueryInsightsResponse"]
            )
        )
    if "ErrorReportLocation" in data:
        import capo_timestream_query.types.error_report_location

        out["error_report_location"] = (
            capo_timestream_query.types.error_report_location.deserialize_aws_json_1_0(
                data["ErrorReportLocation"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
