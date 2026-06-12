"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FieldIndexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.field_index

FieldIndexes: TypeAlias = list["aws_sdk_cloudwatch_logs.types.field_index.FieldIndex"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldIndexes) -> list:
    import aws_sdk_cloudwatch_logs.types.field_index

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.field_index.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FieldIndexes:
    import aws_sdk_cloudwatch_logs.types.field_index

    out: FieldIndexes = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.field_index.deserialize_aws_json_1_1(item)
        )
    return out
