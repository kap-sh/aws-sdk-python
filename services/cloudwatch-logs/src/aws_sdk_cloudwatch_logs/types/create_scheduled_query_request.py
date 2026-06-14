"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateScheduledQueryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.destination_configuration
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
    import aws_sdk_cloudwatch_logs.types.tags
    import aws_sdk_cloudwatch_logs.types.timestamp


class CreateScheduledQueryRequest(TypedDict):
    name: "aws_sdk_cloudwatch_logs.types.scheduled_query_name.ScheduledQueryName"
    """<p>The name of the scheduled query. The name must be unique within your account and region. Valid characters are alphanumeric characters, hyphens, underscores, and periods. Length must be between 1 and 255 characters.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_description.ScheduledQueryDescription"
    ]
    """<p>An optional description for the scheduled query to help identify its purpose and functionality.</p>"""
    query_language: "aws_sdk_cloudwatch_logs.types.query_language.QueryLanguage"
    """<p>The query language to use for the scheduled query. Valid values are <code>CWLI</code>, <code>PPL</code>, and <code>SQL</code>.</p>"""
    query_string: "aws_sdk_cloudwatch_logs.types.query_string.QueryString"
    """<p>The query string to execute. This is the same query syntax used in CloudWatch Logs Insights. Maximum length is 10,000 characters.</p>"""
    log_group_identifiers: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers.ScheduledQueryLogGroupIdentifiers"
    ]
    """<p>An array of log group names or ARNs to query. You can specify between 1 and 50 log groups. Log groups can be identified by name or full ARN.</p>"""
    schedule_expression: (
        "aws_sdk_cloudwatch_logs.types.schedule_expression.ScheduleExpression"
    )
    """<p>A cron expression that defines when the scheduled query runs. The expression uses standard cron syntax and supports minute-level precision. Maximum length is 256 characters.</p>"""
    timezone: NotRequired[
        "aws_sdk_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
    ]
    """<p>The timezone for evaluating the schedule expression. This determines when the scheduled query executes relative to the specified timezone.</p>"""
    start_time_offset: NotRequired[
        "aws_sdk_cloudwatch_logs.types.start_time_offset.StartTimeOffset"
    ]
    """<p>The time offset in seconds that defines the lookback period for the query. This determines how far back in time the query searches from the execution time.</p>"""
    destination_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
    ]
    """<p>Configuration for where to deliver query results. Currently supports Amazon S3 destinations for storing query output.</p>"""
    schedule_start_time: NotRequired[
        "aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"
    ]
    """<p>The start time for the scheduled query in Unix epoch format. The query will not execute before this time.</p>"""
    schedule_end_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The end time for the scheduled query in Unix epoch format. The query will stop executing after this time.</p>"""
    execution_role_arn: "aws_sdk_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants permissions to execute the query and deliver results to the specified destination. The role must have permissions to read from the specified log groups and write to the destination.</p>"""
    state: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
    ]
    """<p>The initial state of the scheduled query. Valid values are <code>ENABLED</code> and <code>DISABLED</code>. Default is <code>ENABLED</code>.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>Key-value pairs to associate with the scheduled query for resource management and cost allocation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScheduledQueryRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_cloudwatch_logs.types.query_language

    out["queryLanguage"] = (
        aws_sdk_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
            value["query_language"]
        )
    )
    out["queryString"] = value["query_string"]
    if "log_group_identifiers" in value:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers

        out["logGroupIdentifiers"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers.serialize_aws_json_1_1(
                value["log_group_identifiers"]
            )
        )
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
    if "schedule_start_time" in value:
        out["scheduleStartTime"] = value["schedule_start_time"]
    if "schedule_end_time" in value:
        out["scheduleEndTime"] = value["schedule_end_time"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "state" in value:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScheduledQueryRequest:
    out: CreateScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateScheduledQueryRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "queryLanguage" in data:
        import aws_sdk_cloudwatch_logs.types.query_language

        out["query_language"] = (
            aws_sdk_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.query_language required"
        )
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("CreateScheduledQueryRequest.query_string required")
    if "logGroupIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers

        out["log_group_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    if "scheduleExpression" in data:
        out["schedule_expression"] = data["scheduleExpression"]
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.schedule_expression required"
        )
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
    if "scheduleStartTime" in data:
        out["schedule_start_time"] = data["scheduleStartTime"]
    if "scheduleEndTime" in data:
        out["schedule_end_time"] = data["scheduleEndTime"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.execution_role_arn required"
        )
    if "state" in data:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
