"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetLoadStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationEventDatasetLoadStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_json(value: DataIntegrationEventDatasetLoadStatus) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationEventDatasetLoadStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationEventDatasetLoadStatus value: {data!r}"
        )
    return cast(DataIntegrationEventDatasetLoadStatus, data)
