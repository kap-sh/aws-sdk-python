"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FilteredLogEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.filtered_log_event

FilteredLogEvents: TypeAlias = list[
    "capo_cloudwatch_logs.types.filtered_log_event.FilteredLogEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilteredLogEvents) -> list:
    import capo_cloudwatch_logs.types.filtered_log_event

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.filtered_log_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FilteredLogEvents:
    import capo_cloudwatch_logs.types.filtered_log_event

    out: FilteredLogEvents = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.filtered_log_event.deserialize_aws_json_1_1(item)
        )
    return out
