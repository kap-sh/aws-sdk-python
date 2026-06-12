"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.result_rows

QueryResults: TypeAlias = list["aws_sdk_cloudwatch_logs.types.result_rows.ResultRows"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResults) -> list:
    import aws_sdk_cloudwatch_logs.types.result_rows

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.result_rows.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueryResults:
    import aws_sdk_cloudwatch_logs.types.result_rows

    out: QueryResults = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.result_rows.deserialize_aws_json_1_1(item)
        )
    return out
