"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogFieldsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_fields_list_item

LogFieldsList: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.log_fields_list_item.LogFieldsListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogFieldsList) -> list:
    import aws_sdk_cloudwatch_logs.types.log_fields_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.log_fields_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogFieldsList:
    import aws_sdk_cloudwatch_logs.types.log_fields_list_item

    out: LogFieldsList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.log_fields_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
