"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintOptimizationJobStatus``."""

from typing import Literal, TypeAlias, cast

"""List of status supported by optimization jobs"""
BlueprintOptimizationJobStatus: TypeAlias = Literal[
    "Created",
    "InProgress",
    "Success",
    "ServiceError",
    "ClientError",
]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintOptimizationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> BlueprintOptimizationJobStatus:
    return cast(BlueprintOptimizationJobStatus, data)
