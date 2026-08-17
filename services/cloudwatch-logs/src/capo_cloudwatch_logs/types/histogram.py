"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Histogram``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.count
    import capo_cloudwatch_logs.types.time

Histogram: TypeAlias = dict[
    "capo_cloudwatch_logs.types.time.Time", "capo_cloudwatch_logs.types.count.Count"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Histogram) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Histogram:
    out: Histogram = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
