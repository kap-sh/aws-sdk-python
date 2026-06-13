"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationFlowTargetType: TypeAlias = Literal[
    "S3",
    "DATASET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "DATASET",
    )
)


def serialize_json(value: DataIntegrationFlowTargetType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowTargetType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationFlowTargetType value: {data!r}"
        )
    return cast(DataIntegrationFlowTargetType, data)
