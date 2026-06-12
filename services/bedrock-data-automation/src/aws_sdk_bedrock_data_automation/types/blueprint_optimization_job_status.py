"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintOptimizationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""List of status supported by optimization jobs"""
BlueprintOptimizationJobStatus: TypeAlias = Literal[
    "Created",
    "InProgress",
    "Success",
    "ServiceError",
    "ClientError",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Created",
        "InProgress",
        "Success",
        "ServiceError",
        "ClientError",
    )
)


def serialize_json(value: BlueprintOptimizationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> BlueprintOptimizationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BlueprintOptimizationJobStatus value: {data!r}"
        )
    return cast(BlueprintOptimizationJobStatus, data)
