"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDeploymentPatternStatus``."""

from typing import Literal, TypeAlias, cast

WorkloadDeploymentPatternStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DISABLED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDeploymentPatternStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkloadDeploymentPatternStatus:
    return cast(WorkloadDeploymentPatternStatus, data)
