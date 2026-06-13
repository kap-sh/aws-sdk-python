"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#MixedInstanceConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.mixed_instance_configuration

MixedInstanceConfigurationList: TypeAlias = list[
    "aws_sdk_cost_optimization_hub.types.mixed_instance_configuration.MixedInstanceConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MixedInstanceConfigurationList) -> list:
    import aws_sdk_cost_optimization_hub.types.mixed_instance_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_optimization_hub.types.mixed_instance_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MixedInstanceConfigurationList:
    import aws_sdk_cost_optimization_hub.types.mixed_instance_configuration

    out: MixedInstanceConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_cost_optimization_hub.types.mixed_instance_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out
