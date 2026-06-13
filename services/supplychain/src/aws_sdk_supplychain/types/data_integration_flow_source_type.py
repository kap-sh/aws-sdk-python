"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationFlowSourceType: TypeAlias = Literal[
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


def serialize_json(value: DataIntegrationFlowSourceType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationFlowSourceType value: {data!r}"
        )
    return cast(DataIntegrationFlowSourceType, data)
