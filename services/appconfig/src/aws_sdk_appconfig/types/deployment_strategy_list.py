"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.deployment_strategy

DeploymentStrategyList: TypeAlias = list[
    "aws_sdk_appconfig.types.deployment_strategy.DeploymentStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategyList) -> list:
    import aws_sdk_appconfig.types.deployment_strategy

    out: list = []
    for item in value:
        out.append(aws_sdk_appconfig.types.deployment_strategy.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeploymentStrategyList:
    import aws_sdk_appconfig.types.deployment_strategy

    out: DeploymentStrategyList = []
    for item in data:
        out.append(aws_sdk_appconfig.types.deployment_strategy.deserialize_json(item))
    return out
