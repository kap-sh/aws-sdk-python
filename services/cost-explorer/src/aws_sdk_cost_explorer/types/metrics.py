"""Generated from Smithy shape ``com.amazonaws.costexplorer#Metrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.metric_name
    import aws_sdk_cost_explorer.types.metric_value

Metrics: TypeAlias = dict[
    "aws_sdk_cost_explorer.types.metric_name.MetricName",
    "aws_sdk_cost_explorer.types.metric_value.MetricValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Metrics) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_cost_explorer.types.metric_value

        out[key] = aws_sdk_cost_explorer.types.metric_value.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Metrics:
    out: Metrics = {}
    for key, value in data.items():
        import aws_sdk_cost_explorer.types.metric_value

        out[key] = aws_sdk_cost_explorer.types.metric_value.deserialize_aws_json_1_1(
            value
        )
    return out
