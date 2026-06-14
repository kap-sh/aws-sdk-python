"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetScheduledQueryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.destination_configuration
    import aws_sdk_cloudwatch_logs.types.execution_status
    import aws_sdk_cloudwatch_logs.types.query_language
    import aws_sdk_cloudwatch_logs.types.query_string
    import aws_sdk_cloudwatch_logs.types.role_arn
    import aws_sdk_cloudwatch_logs.types.schedule_expression
    import aws_sdk_cloudwatch_logs.types.schedule_timezone
    import aws_sdk_cloudwatch_logs.types.scheduled_query_description
    import aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers
    import aws_sdk_cloudwatch_logs.types.scheduled_query_name
    import aws_sdk_cloudwatch_logs.types.scheduled_query_state
    import aws_sdk_cloudwatch_logs.types.start_time_offset
    import aws_sdk_cloudwatch_logs.types.timestamp


class GetScheduledQueryResponse(TypedDict):
    scheduled_query_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the scheduled query.</p>"""
    name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_name.ScheduledQueryName"
    ]
    """<p>The name of the scheduled query.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_description.ScheduledQueryDescription"
    ]
    """<p>The description of the scheduled query.</p>"""
    query_language: NotRequired[
        "aws_sdk_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    """<p>The query language used by the scheduled query.</p>"""
    query_string: NotRequired["aws_sdk_cloudwatch_logs.types.query_string.QueryString"]
    """<p>The query string executed by the scheduled query.</p>"""
    log_group_identifiers: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers.ScheduledQueryLogGroupIdentifiers"
    ]
    """<p>The log groups queried by the scheduled query.</p>"""
    schedule_expression: NotRequired[
        "aws_sdk_cloudwatch_logs.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The cron expression that defines when the scheduled query runs.</p>"""
    timezone: NotRequired[
        "aws_sdk_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
    ]
    """<p>The timezone used for evaluating the schedule expression.</p>"""
    start_time_offset: NotRequired[
        "aws_sdk_cloudwatch_logs.types.start_time_offset.StartTimeOffset"
    ]
    """<p>The time offset in seconds that defines the lookback period for the query.</p>"""
    destination_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
    ]
    """<p>Configuration for where query results are delivered.</p>"""
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
    """<p>The status of the most recent execution of the scheduled query.</p>"""
    schedule_start_time: NotRequired[
        "aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"
    ]
    """<p>The start time for the scheduled query in Unix epoch format.</p>"""
    schedule_end_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The end time for the scheduled query in Unix epoch format.</p>"""
    execution_role_arn: NotRequired["aws_sdk_cloudwatch_logs.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role used to execute the query and deliver results.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the scheduled query was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the scheduled query was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScheduledQueryResponse) -> dict:
    out: dict = {}
    if "scheduled_query_arn" in value:
        out["scheduledQueryArn"] = value["scheduled_query_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "query_language" in value:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            aws_sdk_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "log_group_identifiers" in value:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers

        out["logGroupIdentifiers"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers.serialize_aws_json_1_1(
                value["log_group_identifiers"]
            )
        )
    if "schedule_expression" in value:
        out["scheduleExpression"] = value["schedule_expression"]
    if "timezone" in value:
        out["timezone"] = value["timezone"]
    if "start_time_offset" in value:
        out["startTimeOffset"] = value["start_time_offset"]
    if "destination_configuration" in value:
        import aws_sdk_cloudwatch_logs.types.destination_configuration

        out["destinationConfiguration"] = (
            aws_sdk_cloudwatch_logs.types.destination_configuration.serialize_aws_json_1_1(
                value["destination_configuration"]
            )
        )
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
    if "schedule_start_time" in value:
        out["scheduleStartTime"] = value["schedule_start_time"]
    if "schedule_end_time" in value:
        out["scheduleEndTime"] = value["schedule_end_time"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScheduledQueryResponse:
    out: GetScheduledQueryResponse = {}  # type: ignore[typeddict-item]
    if "scheduledQueryArn" in data:
        out["scheduled_query_arn"] = data["scheduledQueryArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "queryLanguage" in data:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["query_language"] = (
            aws_sdk_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "logGroupIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers

        out["log_group_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    if "scheduleExpression" in data:
        out["schedule_expression"] = data["scheduleExpression"]
    if "timezone" in data:
        out["timezone"] = data["timezone"]
    if "startTimeOffset" in data:
        out["start_time_offset"] = data["startTimeOffset"]
    if "destinationConfiguration" in data:
        import aws_sdk_cloudwatch_logs.types.destination_configuration

        out["destination_configuration"] = (
            aws_sdk_cloudwatch_logs.types.destination_configuration.deserialize_aws_json_1_1(
                data["destinationConfiguration"]
            )
        )
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
    if "scheduleStartTime" in data:
        out["schedule_start_time"] = data["scheduleStartTime"]
    if "scheduleEndTime" in data:
        out["schedule_end_time"] = data["scheduleEndTime"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out
