"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TransformedLogs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.transformed_log_record

TransformedLogs: TypeAlias = list[
    "capo_cloudwatch_logs.types.transformed_log_record.TransformedLogRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformedLogs) -> list:
    import capo_cloudwatch_logs.types.transformed_log_record

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.transformed_log_record.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TransformedLogs:
    import capo_cloudwatch_logs.types.transformed_log_record

    out: TransformedLogs = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.transformed_log_record.deserialize_aws_json_1_1(
                item
            )
        )
    return out
