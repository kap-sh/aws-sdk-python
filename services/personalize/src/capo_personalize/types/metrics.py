"""Generated from Smithy shape ``com.amazonaws.personalize#Metrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.metric_name
    import capo_personalize.types.metric_value

Metrics: TypeAlias = dict[
    "capo_personalize.types.metric_name.MetricName",
    "capo_personalize.types.metric_value.MetricValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Metrics) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Metrics:
    out: Metrics = {}
    for key, value in data.items():
        out[key] = value
    return out
