"""Generated from Smithy shape ``com.amazonaws.ecs#MetricConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.metric_configuration

MetricConfigurationList: TypeAlias = list[
    "capo_ecs.types.metric_configuration.MetricConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricConfigurationList) -> list:
    import capo_ecs.types.metric_configuration

    out: list = []
    for item in value:
        out.append(capo_ecs.types.metric_configuration.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricConfigurationList:
    import capo_ecs.types.metric_configuration

    out: MetricConfigurationList = []
    for item in data:
        out.append(capo_ecs.types.metric_configuration.deserialize_aws_json_1_1(item))
    return out
