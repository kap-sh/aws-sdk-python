"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogFieldsListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_field_name
    import aws_sdk_cloudwatch_logs.types.log_field_type


class LogFieldsListItem(TypedDict):
    log_field_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_field_name.LogFieldName"
    ]
    """<p>The name of the log field.</p>"""
    log_field_type: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_field_type.LogFieldType"
    ]
    """<p>The data type information for the log field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogFieldsListItem) -> dict:
    out: dict = {}
    if "log_field_name" in value:
        out["logFieldName"] = value["log_field_name"]
    if "log_field_type" in value:
        import aws_sdk_cloudwatch_logs.types.log_field_type

        out["logFieldType"] = (
            aws_sdk_cloudwatch_logs.types.log_field_type.serialize_aws_json_1_1(
                value["log_field_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogFieldsListItem:
    out: LogFieldsListItem = {}  # type: ignore[typeddict-item]
    if "logFieldName" in data:
        out["log_field_name"] = data["logFieldName"]
    if "logFieldType" in data:
        import aws_sdk_cloudwatch_logs.types.log_field_type

        out["log_field_type"] = (
            aws_sdk_cloudwatch_logs.types.log_field_type.deserialize_aws_json_1_1(
                data["logFieldType"]
            )
        )
    return out
