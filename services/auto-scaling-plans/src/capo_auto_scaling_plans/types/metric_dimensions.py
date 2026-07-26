"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#MetricDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.metric_dimension

MetricDimensions: TypeAlias = list[
    "capo_auto_scaling_plans.types.metric_dimension.MetricDimension"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimensions) -> list:
    import capo_auto_scaling_plans.types.metric_dimension

    out: list = []
    for item in value:
        out.append(
            capo_auto_scaling_plans.types.metric_dimension.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricDimensions:
    import capo_auto_scaling_plans.types.metric_dimension

    out: MetricDimensions = []
    for item in data:
        out.append(
            capo_auto_scaling_plans.types.metric_dimension.deserialize_aws_json_1_1(
                item
            )
        )
    return out
