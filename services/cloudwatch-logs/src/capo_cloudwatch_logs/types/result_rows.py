"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResultRows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.result_field

ResultRows: TypeAlias = list["capo_cloudwatch_logs.types.result_field.ResultField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultRows) -> list:
    import capo_cloudwatch_logs.types.result_field

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.result_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResultRows:
    import capo_cloudwatch_logs.types.result_field

    out: ResultRows = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.result_field.deserialize_aws_json_1_1(item)
        )
    return out
