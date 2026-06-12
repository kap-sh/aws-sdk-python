"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceCapacityProviderStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_service_capacity_provider_strategy_details

AwsEcsServiceCapacityProviderStrategyList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_service_capacity_provider_strategy_details.AwsEcsServiceCapacityProviderStrategyDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceCapacityProviderStrategyList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_service_capacity_provider_strategy_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_capacity_provider_strategy_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsServiceCapacityProviderStrategyList:
    import aws_sdk_securityhub.types.aws_ecs_service_capacity_provider_strategy_details

    out: AwsEcsServiceCapacityProviderStrategyList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_capacity_provider_strategy_details.deserialize_json(
                item
            )
        )
    return out
