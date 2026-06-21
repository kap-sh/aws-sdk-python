"""Generated from Smithy shape ``com.amazonaws.medialive#SignalMapMonitorDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

"""A signal map's monitor deployment status."""
SignalMapMonitorDeploymentStatus: TypeAlias = Literal[
    "NOT_DEPLOYED",
    "DRY_RUN_DEPLOYMENT_COMPLETE",
    "DRY_RUN_DEPLOYMENT_FAILED",
    "DRY_RUN_DEPLOYMENT_IN_PROGRESS",
    "DEPLOYMENT_COMPLETE",
    "DEPLOYMENT_FAILED",
    "DEPLOYMENT_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalMapMonitorDeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> SignalMapMonitorDeploymentStatus:
    return cast(SignalMapMonitorDeploymentStatus, data)
