"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterDefaultCapacityProviderStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details

AwsEcsClusterDefaultCapacityProviderStrategyList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details.AwsEcsClusterDefaultCapacityProviderStrategyDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsClusterDefaultCapacityProviderStrategyList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsClusterDefaultCapacityProviderStrategyList:
    import aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details

    out: AwsEcsClusterDefaultCapacityProviderStrategyList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details.deserialize_json(
                item
            )
        )
    return out
