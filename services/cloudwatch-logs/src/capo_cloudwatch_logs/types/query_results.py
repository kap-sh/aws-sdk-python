"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.result_rows

QueryResults: TypeAlias = list["capo_cloudwatch_logs.types.result_rows.ResultRows"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResults) -> list:
    import capo_cloudwatch_logs.types.result_rows

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.result_rows.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueryResults:
    import capo_cloudwatch_logs.types.result_rows

    out: QueryResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.result_rows.deserialize_aws_json_1_1(item)
        )
    return out
