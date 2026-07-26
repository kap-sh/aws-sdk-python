"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetScheduledQueryHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.scheduled_query_name
    import capo_cloudwatch_logs.types.trigger_history_record_list


class GetScheduledQueryHistoryResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_name.ScheduledQueryName"
    ]
    """<p>The name of the scheduled query.</p>"""
    scheduled_query_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the scheduled query.</p>"""
    trigger_history: NotRequired[
        "capo_cloudwatch_logs.types.trigger_history_record_list.TriggerHistoryRecordList"
    ]
    """<p>An array of execution history records for the scheduled query.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScheduledQueryHistoryResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "scheduled_query_arn" in value:
        out["scheduledQueryArn"] = value["scheduled_query_arn"]
    if "trigger_history" in value:
        import capo_cloudwatch_logs.types.trigger_history_record_list

        out["triggerHistory"] = (
            capo_cloudwatch_logs.types.trigger_history_record_list.serialize_aws_json_1_1(
                value["trigger_history"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScheduledQueryHistoryResponse:
    out: GetScheduledQueryHistoryResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "scheduledQueryArn" in data:
        out["scheduled_query_arn"] = data["scheduledQueryArn"]
    if "triggerHistory" in data:
        import capo_cloudwatch_logs.types.trigger_history_record_list

        out["trigger_history"] = (
            capo_cloudwatch_logs.types.trigger_history_record_list.deserialize_aws_json_1_1(
                data["triggerHistory"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
