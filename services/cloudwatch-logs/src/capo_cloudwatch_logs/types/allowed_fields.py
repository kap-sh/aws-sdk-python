"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AllowedFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.record_field

AllowedFields: TypeAlias = list["capo_cloudwatch_logs.types.record_field.RecordField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedFields) -> list:
    import capo_cloudwatch_logs.types.record_field

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.record_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AllowedFields:
    import capo_cloudwatch_logs.types.record_field

    out: AllowedFields = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.record_field.deserialize_aws_json_1_1(item)
        )
    return out
