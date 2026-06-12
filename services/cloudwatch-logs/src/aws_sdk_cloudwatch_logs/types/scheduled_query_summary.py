"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduledQuerySummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.destination_configuration
    import aws_sdk_cloudwatch_logs.types.execution_status
    import aws_sdk_cloudwatch_logs.types.schedule_expression
    import aws_sdk_cloudwatch_logs.types.schedule_timezone
    import aws_sdk_cloudwatch_logs.types.scheduled_query_name
    import aws_sdk_cloudwatch_logs.types.scheduled_query_state
    import aws_sdk_cloudwatch_logs.types.timestamp


class ScheduledQuerySummary(TypedDict):
    scheduled_query_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the scheduled query.</p>"""
    name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_name.ScheduledQueryName"
    ]
    """<p>The name of the scheduled query.</p>"""
    state: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
    ]
    """<p>The current state of the scheduled query.</p>"""
    last_triggered_time: NotRequired[
        "aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"
    ]
    """<p>The timestamp when the scheduled query was last executed.</p>"""
    last_execution_status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.execution_status.ExecutionStatus"
    ]
    """<p>The status of the most recent execution.</p>"""
    schedule_expression: NotRequired[
        "aws_sdk_cloudwatch_logs.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The cron expression that defines when the scheduled query runs.</p>"""
    timezone: NotRequired[
        "aws_sdk_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
    ]
    """<p>The timezone used for evaluating the schedule expression.</p>"""
    destination_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
    ]
    """<p>Configuration for where query results are delivered.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the scheduled query was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the scheduled query was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledQuerySummary) -> dict:
    out: dict = {}
    if "scheduled_query_arn" in value:
        out["scheduledQueryArn"] = value["scheduled_query_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "state" in value:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "last_triggered_time" in value:
        out["lastTriggeredTime"] = value["last_triggered_time"]
    if "last_execution_status" in value:
        import aws_sdk_cloudwatch_logs.types.execution_status

        out["lastExecutionStatus"] = (
            aws_sdk_cloudwatch_logs.types.execution_status.serialize_aws_json_1_1(
                value["last_execution_status"]
            )
        )
    if "schedule_expression" in value:
        out["scheduleExpression"] = value["schedule_expression"]
    if "timezone" in value:
        out["timezone"] = value["timezone"]
    if "destination_configuration" in value:
        import aws_sdk_cloudwatch_logs.types.destination_configuration

        out["destinationConfiguration"] = (
            aws_sdk_cloudwatch_logs.types.destination_configuration.serialize_aws_json_1_1(
                value["destination_configuration"]
            )
        )
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduledQuerySummary:
    out: ScheduledQuerySummary = {}  # type: ignore[typeddict-item]
    if "scheduledQueryArn" in data:
        out["scheduled_query_arn"] = data["scheduledQueryArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "state" in data:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    if "lastTriggeredTime" in data:
        out["last_triggered_time"] = data["lastTriggeredTime"]
    if "lastExecutionStatus" in data:
        import aws_sdk_cloudwatch_logs.types.execution_status

        out["last_execution_status"] = (
            aws_sdk_cloudwatch_logs.types.execution_status.deserialize_aws_json_1_1(
                data["lastExecutionStatus"]
            )
        )
    if "scheduleExpression" in data:
        out["schedule_expression"] = data["scheduleExpression"]
    if "timezone" in data:
        out["timezone"] = data["timezone"]
    if "destinationConfiguration" in data:
        import aws_sdk_cloudwatch_logs.types.destination_configuration

        out["destination_configuration"] = (
            aws_sdk_cloudwatch_logs.types.destination_configuration.deserialize_aws_json_1_1(
                data["destinationConfiguration"]
            )
        )
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out
