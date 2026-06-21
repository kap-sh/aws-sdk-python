"""Generated from Smithy shape ``com.amazonaws.greengrassv2#EffectiveDeploymentExecutionStatus``."""

from typing import Literal, TypeAlias, cast

EffectiveDeploymentExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "QUEUED",
    "FAILED",
    "COMPLETED",
    "TIMED_OUT",
    "CANCELED",
    "REJECTED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveDeploymentExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> EffectiveDeploymentExecutionStatus:
    return cast(EffectiveDeploymentExecutionStatus, data)
