"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterDefaultCapacityProviderStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details

AwsEcsClusterDefaultCapacityProviderStrategyList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details.AwsEcsClusterDefaultCapacityProviderStrategyDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsClusterDefaultCapacityProviderStrategyList) -> list:
    import capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsClusterDefaultCapacityProviderStrategyList:
    import capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details

    out: AwsEcsClusterDefaultCapacityProviderStrategyList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_details.deserialize_json(
                item
            )
        )
    return out
