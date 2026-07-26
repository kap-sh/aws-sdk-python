"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsClusterStatus``."""

from typing import Literal, TypeAlias, cast

EcsClusterStatus: TypeAlias = Literal[
    "ACTIVE",
    "PROVISIONING",
    "DEPROVISIONING",
    "FAILED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> EcsClusterStatus:
    return cast(EcsClusterStatus, data)
