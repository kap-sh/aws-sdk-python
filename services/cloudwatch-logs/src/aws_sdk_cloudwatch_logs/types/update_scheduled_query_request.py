"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateScheduledQueryRequest``."""

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
    import aws_sdk_cloudwatch_logs.types.scheduled_query_identifier
    import aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers
    import aws_sdk_cloudwatch_logs.types.scheduled_query_state
    import aws_sdk_cloudwatch_logs.types.start_time_offset
    import aws_sdk_cloudwatch_logs.types.timestamp


class UpdateScheduledQueryRequest(TypedDict):
    identifier: "aws_sdk_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier"
    """<p>The ARN or name of the scheduled query to update.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_description.ScheduledQueryDescription"
    ]
    """<p>An updated description for the scheduled query.</p>"""
    query_language: "aws_sdk_cloudwatch_logs.types.query_language.QueryLanguage"
    """<p>The updated query language for the scheduled query.</p>"""
    query_string: "aws_sdk_cloudwatch_logs.types.query_string.QueryString"
    """<p>The updated query string to execute.</p>"""
    log_group_identifiers: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_log_group_identifiers.ScheduledQueryLogGroupIdentifiers"
    ]
    """<p>The updated array of log group names or ARNs to query.</p>"""
    schedule_expression: (
        "aws_sdk_cloudwatch_logs.types.schedule_expression.ScheduleExpression"
    )
    """<p>The updated cron expression that defines when the scheduled query runs.</p>"""
    timezone: NotRequired[
        "aws_sdk_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
    ]
    """<p>The updated timezone for evaluating the schedule expression.</p>"""
    start_time_offset: NotRequired[
        "aws_sdk_cloudwatch_logs.types.start_time_offset.StartTimeOffset"
    ]
    """<p>The updated time offset in seconds that defines the lookback period for the query.</p>"""
    destination_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
    ]
    """<p>The updated configuration for where to deliver query results.</p>"""
    schedule_start_time: NotRequired[
        "aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"
    ]
    """<p>The updated start time for the scheduled query in Unix epoch format.</p>"""
    schedule_end_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The updated end time for the scheduled query in Unix epoch format.</p>"""
    execution_role_arn: "aws_sdk_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The updated ARN of the IAM role that grants permissions to execute the query and deliver results.</p>"""
    state: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
    ]
    """<p>The updated state of the scheduled query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScheduledQueryRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateScheduledQueryRequest:
    out: UpdateScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("UpdateScheduledQueryRequest.identifier required")
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
            "UpdateScheduledQueryRequest.query_language required"
        )
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("UpdateScheduledQueryRequest.query_string required")
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
            "UpdateScheduledQueryRequest.schedule_expression required"
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
            "UpdateScheduledQueryRequest.execution_role_arn required"
        )
    if "state" in data:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    return out
