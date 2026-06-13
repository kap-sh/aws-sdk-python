"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowTransformationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationFlowTransformationType: TypeAlias = Literal[
    "SQL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SQL",
        "NONE",
    )
)


def serialize_json(value: DataIntegrationFlowTransformationType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowTransformationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationFlowTransformationType value: {data!r}"
        )
    return cast(DataIntegrationFlowTransformationType, data)
