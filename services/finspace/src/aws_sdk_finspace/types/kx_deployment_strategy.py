"""Generated from Smithy shape ``com.amazonaws.finspace#KxDeploymentStrategy``."""

from typing import Literal, TypeAlias, cast

KxDeploymentStrategy: TypeAlias = Literal[
    "NO_RESTART",
    "ROLLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDeploymentStrategy) -> str:
    return value


def deserialize_json(data: str) -> KxDeploymentStrategy:
    return cast(KxDeploymentStrategy, data)
