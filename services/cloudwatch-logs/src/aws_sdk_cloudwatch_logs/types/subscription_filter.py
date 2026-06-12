"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SubscriptionFilter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.apply_on_transformed_logs
    import aws_sdk_cloudwatch_logs.types.destination_arn
    import aws_sdk_cloudwatch_logs.types.distribution
    import aws_sdk_cloudwatch_logs.types.emit_system_fields
    import aws_sdk_cloudwatch_logs.types.field_selection_criteria
    import aws_sdk_cloudwatch_logs.types.filter_name
    import aws_sdk_cloudwatch_logs.types.filter_pattern
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.role_arn
    import aws_sdk_cloudwatch_logs.types.timestamp


class SubscriptionFilter(TypedDict):
    filter_name: NotRequired["aws_sdk_cloudwatch_logs.types.filter_name.FilterName"]
    """<p>The name of the subscription filter.</p>"""
    log_group_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p>"""
    filter_pattern: NotRequired[
        "aws_sdk_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    destination_arn: NotRequired[
        "aws_sdk_cloudwatch_logs.types.destination_arn.DestinationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the destination.</p>"""
    role_arn: NotRequired["aws_sdk_cloudwatch_logs.types.role_arn.RoleArn"]
    """<p></p>"""
    distribution: NotRequired["aws_sdk_cloudwatch_logs.types.distribution.Distribution"]
    apply_on_transformed_logs: (
        "aws_sdk_cloudwatch_logs.types.apply_on_transformed_logs.ApplyOnTransformedLogs"
    )
    """<p>This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html\">PutTransformer</a>.</p> <p>If this value is <code>true</code>, the subscription filter is applied on the transformed version of the log events instead of the original ingested log events.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The creation time of the subscription filter, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    field_selection_criteria: NotRequired[
        "aws_sdk_cloudwatch_logs.types.field_selection_criteria.FieldSelectionCriteria"
    ]
    """<p>The filter expression that specifies which log events are processed by this subscription filter based on system fields. Returns the <code>fieldSelectionCriteria</code> value if it was specified when the subscription filter was created.</p>"""
    emit_system_fields: NotRequired[
        "aws_sdk_cloudwatch_logs.types.emit_system_fields.EmitSystemFields"
    ]
    """<p>The list of system fields that are included in the log events sent to the subscription destination. Returns the <code>emitSystemFields</code> value if it was specified when the subscription filter was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionFilter) -> dict:
    out: dict = {}
    if "filter_name" in value:
        out["filterName"] = value["filter_name"]
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    if "destination_arn" in value:
        out["destinationArn"] = value["destination_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "distribution" in value:
        import aws_sdk_cloudwatch_logs.types.distribution

        out["distribution"] = (
            aws_sdk_cloudwatch_logs.types.distribution.serialize_aws_json_1_1(
                value["distribution"]
            )
        )
    out["applyOnTransformedLogs"] = value.get("apply_on_transformed_logs", False)
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "field_selection_criteria" in value:
        out["fieldSelectionCriteria"] = value["field_selection_criteria"]
    if "emit_system_fields" in value:
        import aws_sdk_cloudwatch_logs.types.emit_system_fields

        out["emitSystemFields"] = (
            aws_sdk_cloudwatch_logs.types.emit_system_fields.serialize_aws_json_1_1(
                value["emit_system_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscriptionFilter:
    out: SubscriptionFilter = {}  # type: ignore[typeddict-item]
    if "filterName" in data:
        out["filter_name"] = data["filterName"]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "filterPattern" in data:
        out["filter_pattern"] = data["filterPattern"]
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "distribution" in data:
        import aws_sdk_cloudwatch_logs.types.distribution

        out["distribution"] = (
            aws_sdk_cloudwatch_logs.types.distribution.deserialize_aws_json_1_1(
                data["distribution"]
            )
        )
    if "applyOnTransformedLogs" in data:
        out["apply_on_transformed_logs"] = data["applyOnTransformedLogs"]
    else:
        out["apply_on_transformed_logs"] = False
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "fieldSelectionCriteria" in data:
        out["field_selection_criteria"] = data["fieldSelectionCriteria"]
    if "emitSystemFields" in data:
        import aws_sdk_cloudwatch_logs.types.emit_system_fields

        out["emit_system_fields"] = (
            aws_sdk_cloudwatch_logs.types.emit_system_fields.deserialize_aws_json_1_1(
                data["emitSystemFields"]
            )
        )
    return out
