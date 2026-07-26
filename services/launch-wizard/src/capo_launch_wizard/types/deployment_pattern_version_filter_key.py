"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentPatternVersionFilterKey``."""

from typing import Literal, TypeAlias, cast

DeploymentPatternVersionFilterKey: TypeAlias = Literal["updateFromVersion",]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentPatternVersionFilterKey) -> str:
    return value


def deserialize_json(data: str) -> DeploymentPatternVersionFilterKey:
    return cast(DeploymentPatternVersionFilterKey, data)
