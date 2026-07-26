"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusterCodeDeploymentStrategy``."""

from typing import Literal, TypeAlias, cast

KxClusterCodeDeploymentStrategy: TypeAlias = Literal[
    "NO_RESTART",
    "ROLLING",
    "FORCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxClusterCodeDeploymentStrategy) -> str:
    return value


def deserialize_json(data: str) -> KxClusterCodeDeploymentStrategy:
    return cast(KxClusterCodeDeploymentStrategy, data)
