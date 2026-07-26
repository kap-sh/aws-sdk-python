"""Generated from Smithy shape ``com.amazonaws.opensearch#DeploymentStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the deployment strategy for the domain. Valid values are <code>Default</code> and <code>CapacityOptimized</code>.</p>"""
DeploymentStrategy: TypeAlias = Literal[
    "Default",
    "CapacityOptimized",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategy) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStrategy:
    return cast(DeploymentStrategy, data)
