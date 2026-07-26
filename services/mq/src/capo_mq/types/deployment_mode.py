"""Generated from Smithy shape ``com.amazonaws.mq#DeploymentMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The broker's deployment mode.</p>"""
DeploymentMode: TypeAlias = Literal[
    "SINGLE_INSTANCE",
    "ACTIVE_STANDBY_MULTI_AZ",
    "CLUSTER_MULTI_AZ",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentMode) -> str:
    return value


def deserialize_json(data: str) -> DeploymentMode:
    return cast(DeploymentMode, data)
