"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateScheduledQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.destination_configuration
    import capo_cloudwatch_logs.types.execution_status
    import capo_cloudwatch_logs.types.query_language
    import capo_cloudwatch_logs.types.query_string
    import capo_cloudwatch_logs.types.role_arn
    import capo_cloudwatch_logs.types.schedule_expression
    import capo_cloudwatch_logs.types.schedule_timezone
    import capo_cloudwatch_logs.types.scheduled_query_description
    import capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers
    import capo_cloudwatch_logs.types.scheduled_query_name
    import capo_cloudwatch_logs.types.scheduled_query_state
    import capo_cloudwatch_logs.types.start_time_offset
    import capo_cloudwatch_logs.types.timestamp


class UpdateScheduledQueryResponse(TypedDict, closed=True):
    scheduled_query_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the updated scheduled query.</p>"""
    name: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_name.ScheduledQueryName"
    ]
    """<p>The name of the updated scheduled query.</p>"""
    description: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_description.ScheduledQueryDescription"
    ]
    """<p>The description of the updated scheduled query.</p>"""
    query_language: NotRequired[
        "capo_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    """<p>The query language of the updated scheduled query.</p>"""
    query_string: NotRequired["capo_cloudwatch_logs.types.query_string.QueryString"]
    """<p>The query string of the updated scheduled query.</p>"""
    log_group_identifiers: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.ScheduledQueryLogGroupIdentifiers"
    ]
    """<p>The log groups queried by the updated scheduled query.</p>"""
    schedule_expression: NotRequired[
        "capo_cloudwatch_logs.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The cron expression of the updated scheduled query.</p>"""
    timezone: NotRequired[
        "capo_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
    ]
    """<p>The timezone of the updated scheduled query.</p>"""
    start_time_offset: NotRequired[
        "capo_cloudwatch_logs.types.start_time_offset.StartTimeOffset"
    ]
    """<p>The time offset of the updated scheduled query.</p>"""
    destination_configuration: NotRequired[
        "capo_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
    ]
    """<p>The destination configuration of the updated scheduled query.</p>"""
    state: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
    ]
    """<p>The state of the updated scheduled query.</p>"""
    last_triggered_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the updated scheduled query was last executed.</p>"""
    last_execution_status: NotRequired[
        "capo_cloudwatch_logs.types.execution_status.ExecutionStatus"
    ]
    """<p>The status of the most recent execution of the updated scheduled query.</p>"""
    schedule_start_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The start time of the updated scheduled query.</p>"""
    schedule_end_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The end time of the updated scheduled query.</p>"""
    execution_role_arn: NotRequired["capo_cloudwatch_logs.types.role_arn.RoleArn"]
    """<p>The execution role ARN of the updated scheduled query.</p>"""
    creation_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the scheduled query was originally created.</p>"""
    last_updated_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the scheduled query was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScheduledQueryResponse) -> dict:
    out: dict = {}
    if "scheduled_query_arn" in value:
        out["scheduledQueryArn"] = value["scheduled_query_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "query_language" in value:
        import capo_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            capo_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "log_group_identifiers" in value:
        import capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers

        out["logGroupIdentifiers"] = (
            capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.serialize_aws_json_1_1(
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
        import capo_cloudwatch_logs.types.destination_configuration

        out["destinationConfiguration"] = (
            capo_cloudwatch_logs.types.destination_configuration.serialize_aws_json_1_1(
                value["destination_configuration"]
            )
        )
    if "state" in value:
        import capo_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            capo_cloudwatch_logs.types.scheduled_query_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "last_triggered_time" in value:
        out["lastTriggeredTime"] = value["last_triggered_time"]
    if "last_execution_status" in value:
        import capo_cloudwatch_logs.types.execution_status

        out["lastExecutionStatus"] = (
            capo_cloudwatch_logs.types.execution_status.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> UpdateScheduledQueryResponse:
    out: UpdateScheduledQueryResponse = {}  # type: ignore[typeddict-item]
    if "scheduledQueryArn" in data:
        out["scheduled_query_arn"] = data["scheduledQueryArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "queryLanguage" in data:
        import capo_cloudwatch_logs.types.query_language

        out["query_language"] = (
            capo_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "logGroupIdentifiers" in data:
        import capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.deserialize_aws_json_1_1(
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
        import capo_cloudwatch_logs.types.destination_configuration

        out["destination_configuration"] = (
            capo_cloudwatch_logs.types.destination_configuration.deserialize_aws_json_1_1(
                data["destinationConfiguration"]
            )
        )
    if "state" in data:
        import capo_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            capo_cloudwatch_logs.types.scheduled_query_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    if "lastTriggeredTime" in data:
        out["last_triggered_time"] = data["lastTriggeredTime"]
    if "lastExecutionStatus" in data:
        import capo_cloudwatch_logs.types.execution_status

        out["last_execution_status"] = (
            capo_cloudwatch_logs.types.execution_status.deserialize_aws_json_1_1(
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
