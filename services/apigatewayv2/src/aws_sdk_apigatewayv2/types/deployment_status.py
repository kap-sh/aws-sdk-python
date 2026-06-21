"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Represents a deployment status.</p>"""
DeploymentStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "DEPLOYED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    return cast(DeploymentStatus, data)
