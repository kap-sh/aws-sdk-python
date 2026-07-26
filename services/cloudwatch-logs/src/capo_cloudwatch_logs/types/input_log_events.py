"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InputLogEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.input_log_event

InputLogEvents: TypeAlias = list[
    "capo_cloudwatch_logs.types.input_log_event.InputLogEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLogEvents) -> list:
    import capo_cloudwatch_logs.types.input_log_event

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.input_log_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InputLogEvents:
    import capo_cloudwatch_logs.types.input_log_event

    out: InputLogEvents = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.input_log_event.deserialize_aws_json_1_1(item)
        )
    return out
