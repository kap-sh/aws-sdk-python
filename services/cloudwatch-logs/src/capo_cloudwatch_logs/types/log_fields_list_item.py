"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogFieldsListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_field_name
    import capo_cloudwatch_logs.types.log_field_type


class LogFieldsListItem(TypedDict, closed=True):
    log_field_name: NotRequired[
        "capo_cloudwatch_logs.types.log_field_name.LogFieldName"
    ]
    """<p>The name of the log field.</p>"""
    log_field_type: NotRequired[
        "capo_cloudwatch_logs.types.log_field_type.LogFieldType"
    ]
    """<p>The data type information for the log field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogFieldsListItem) -> dict:
    out: dict = {}
    if "log_field_name" in value:
        out["logFieldName"] = value["log_field_name"]
    if "log_field_type" in value:
        import capo_cloudwatch_logs.types.log_field_type

        out["logFieldType"] = (
            capo_cloudwatch_logs.types.log_field_type.serialize_aws_json_1_1(
                value["log_field_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogFieldsListItem:
    out: LogFieldsListItem = {}  # type: ignore[typeddict-item]
    if data.get("logFieldName") is not None:
        out["log_field_name"] = data["logFieldName"]
    if data.get("logFieldType") is not None:
        import capo_cloudwatch_logs.types.log_field_type

        out["log_field_type"] = (
            capo_cloudwatch_logs.types.log_field_type.deserialize_aws_json_1_1(
                data["logFieldType"]
            )
        )
    return out
