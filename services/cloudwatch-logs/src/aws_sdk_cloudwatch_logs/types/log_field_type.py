"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogFieldType``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.data_type
    import aws_sdk_cloudwatch_logs.types.log_field_type
    import aws_sdk_cloudwatch_logs.types.log_fields_list


class LogFieldType(TypedDict):
    type: NotRequired["aws_sdk_cloudwatch_logs.types.data_type.DataType"]
    """<p>The data type of the log field.</p>"""
    element: NotRequired["aws_sdk_cloudwatch_logs.types.log_field_type.LogFieldType"]
    """<p>For array or collection types, specifies the element type information.</p>"""
    fields: NotRequired["aws_sdk_cloudwatch_logs.types.log_fields_list.LogFieldsList"]
    """<p>For complex types, contains the nested field definitions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogFieldType) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "element" in value:
        import aws_sdk_cloudwatch_logs.types.log_field_type

        out["element"] = (
            aws_sdk_cloudwatch_logs.types.log_field_type.serialize_aws_json_1_1(
                value["element"]
            )
        )
    if "fields" in value:
        import aws_sdk_cloudwatch_logs.types.log_fields_list

        out["fields"] = (
            aws_sdk_cloudwatch_logs.types.log_fields_list.serialize_aws_json_1_1(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogFieldType:
    out: LogFieldType = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "element" in data:
        import aws_sdk_cloudwatch_logs.types.log_field_type

        out["element"] = (
            aws_sdk_cloudwatch_logs.types.log_field_type.deserialize_aws_json_1_1(
                data["element"]
            )
        )
    if "fields" in data:
        import aws_sdk_cloudwatch_logs.types.log_fields_list

        out["fields"] = (
            aws_sdk_cloudwatch_logs.types.log_fields_list.deserialize_aws_json_1_1(
                data["fields"]
            )
        )
    return out
