"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationEventDatasetOperationType: TypeAlias = Literal[
    "APPEND",
    "UPSERT",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPEND",
        "UPSERT",
        "DELETE",
    )
)


def serialize_json(value: DataIntegrationEventDatasetOperationType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationEventDatasetOperationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationEventDatasetOperationType value: {data!r}"
        )
    return cast(DataIntegrationEventDatasetOperationType, data)
