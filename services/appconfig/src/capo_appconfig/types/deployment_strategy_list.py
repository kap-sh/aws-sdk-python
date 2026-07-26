"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.deployment_strategy

DeploymentStrategyList: TypeAlias = list[
    "capo_appconfig.types.deployment_strategy.DeploymentStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategyList) -> list:
    import capo_appconfig.types.deployment_strategy

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.deployment_strategy.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeploymentStrategyList:
    import capo_appconfig.types.deployment_strategy

    out: DeploymentStrategyList = []
    for item in data:
        out.append(capo_appconfig.types.deployment_strategy.deserialize_json(item))
    return out
