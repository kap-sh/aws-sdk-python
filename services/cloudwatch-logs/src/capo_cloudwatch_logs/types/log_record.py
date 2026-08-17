"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogRecord``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field
    import capo_cloudwatch_logs.types.value

LogRecord: TypeAlias = dict[
    "capo_cloudwatch_logs.types.field.Field", "capo_cloudwatch_logs.types.value.Value"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LogRecord) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LogRecord:
    out: LogRecord = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
