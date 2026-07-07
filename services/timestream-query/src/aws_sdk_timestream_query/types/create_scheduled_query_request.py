"""Generated from Smithy shape ``com.amazonaws.timestreamquery#CreateScheduledQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name
    import aws_sdk_timestream_query.types.client_token
    import aws_sdk_timestream_query.types.error_report_configuration
    import aws_sdk_timestream_query.types.notification_configuration
    import aws_sdk_timestream_query.types.query_string
    import aws_sdk_timestream_query.types.schedule_configuration
    import aws_sdk_timestream_query.types.scheduled_query_name
    import aws_sdk_timestream_query.types.string_value2048
    import aws_sdk_timestream_query.types.tag_list
    import aws_sdk_timestream_query.types.target_configuration


class CreateScheduledQueryRequest(TypedDict, closed=True):
    name: "aws_sdk_timestream_query.types.scheduled_query_name.ScheduledQueryName"
    """<p>Name of the scheduled query.</p>"""
    query_string: "aws_sdk_timestream_query.types.query_string.QueryString"
    """<p>The query string to run. Parameter names can be specified in the query string <code>@</code> character followed by an identifier. The named Parameter <code>@scheduled_runtime</code> is reserved and can be used in the query to get the time at which the query is scheduled to run.</p> <p>The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of <code>@scheduled_runtime</code> paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the <code>@scheduled_runtime</code> parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.</p>"""
    schedule_configuration: (
        "aws_sdk_timestream_query.types.schedule_configuration.ScheduleConfiguration"
    )
    """<p>The schedule configuration for the query.</p>"""
    notification_configuration: "aws_sdk_timestream_query.types.notification_configuration.NotificationConfiguration"
    """<p>Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it. </p>"""
    target_configuration: NotRequired[
        "aws_sdk_timestream_query.types.target_configuration.TargetConfiguration"
    ]
    """<p>Configuration used for writing the result of a query.</p>"""
    client_token: NotRequired["aws_sdk_timestream_query.types.client_token.ClientToken"]
    """<p>Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request. </p> <ul> <li> <p> If CreateScheduledQuery is called without a <code>ClientToken</code>, the Query SDK generates a <code>ClientToken</code> on your behalf.</p> </li> <li> <p> After 8 hours, any request with the same <code>ClientToken</code> is treated as a new request. </p> </li> </ul>"""
    scheduled_query_execution_role_arn: (
        "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN for the IAM role that Timestream will assume when running the scheduled query. </p>"""
    tags: NotRequired["aws_sdk_timestream_query.types.tag_list.TagList"]
    """<p>A list of key-value pairs to label the scheduled query.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_timestream_query.types.string_value2048.StringValue2048"
    ]
    """<p>The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with <i>alias/</i> </p> <p>If ErrorReportConfiguration uses <code>SSE_KMS</code> as encryption type, the same KmsKeyId is used to encrypt the error report at rest.</p>"""
    error_report_configuration: "aws_sdk_timestream_query.types.error_report_configuration.ErrorReportConfiguration"
    """<p>Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateScheduledQueryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["QueryString"] = value["query_string"]
    import aws_sdk_timestream_query.types.schedule_configuration

    out["ScheduleConfiguration"] = (
        aws_sdk_timestream_query.types.schedule_configuration.serialize_aws_json_1_0(
            value["schedule_configuration"]
        )
    )
    import aws_sdk_timestream_query.types.notification_configuration

    out["NotificationConfiguration"] = (
        aws_sdk_timestream_query.types.notification_configuration.serialize_aws_json_1_0(
            value["notification_configuration"]
        )
    )
    if "target_configuration" in value:
        import aws_sdk_timestream_query.types.target_configuration

        out["TargetConfiguration"] = (
            aws_sdk_timestream_query.types.target_configuration.serialize_aws_json_1_0(
                value["target_configuration"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ScheduledQueryExecutionRoleArn"] = value["scheduled_query_execution_role_arn"]
    if "tags" in value:
        import aws_sdk_timestream_query.types.tag_list

        out["Tags"] = aws_sdk_timestream_query.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    import aws_sdk_timestream_query.types.error_report_configuration

    out["ErrorReportConfiguration"] = (
        aws_sdk_timestream_query.types.error_report_configuration.serialize_aws_json_1_0(
            value["error_report_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateScheduledQueryRequest:
    out: CreateScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateScheduledQueryRequest.name required")
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    else:
        raise DeserializationError("CreateScheduledQueryRequest.query_string required")
    if "ScheduleConfiguration" in data:
        import aws_sdk_timestream_query.types.schedule_configuration

        out["schedule_configuration"] = (
            aws_sdk_timestream_query.types.schedule_configuration.deserialize_aws_json_1_0(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.schedule_configuration required"
        )
    if "NotificationConfiguration" in data:
        import aws_sdk_timestream_query.types.notification_configuration

        out["notification_configuration"] = (
            aws_sdk_timestream_query.types.notification_configuration.deserialize_aws_json_1_0(
                data["NotificationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.notification_configuration required"
        )
    if "TargetConfiguration" in data:
        import aws_sdk_timestream_query.types.target_configuration

        out["target_configuration"] = (
            aws_sdk_timestream_query.types.target_configuration.deserialize_aws_json_1_0(
                data["TargetConfiguration"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ScheduledQueryExecutionRoleArn" in data:
        out["scheduled_query_execution_role_arn"] = data[
            "ScheduledQueryExecutionRoleArn"
        ]
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.scheduled_query_execution_role_arn required"
        )
    if "Tags" in data:
        import aws_sdk_timestream_query.types.tag_list

        out["tags"] = aws_sdk_timestream_query.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "ErrorReportConfiguration" in data:
        import aws_sdk_timestream_query.types.error_report_configuration

        out["error_report_configuration"] = (
            aws_sdk_timestream_query.types.error_report_configuration.deserialize_aws_json_1_0(
                data["ErrorReportConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateScheduledQueryRequest.error_report_configuration required"
        )
    return out
