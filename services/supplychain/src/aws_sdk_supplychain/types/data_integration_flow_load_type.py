"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowLoadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationFlowLoadType: TypeAlias = Literal[
    "INCREMENTAL",
    "REPLACE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCREMENTAL",
        "REPLACE",
    )
)


def serialize_json(value: DataIntegrationFlowLoadType) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowLoadType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationFlowLoadType value: {data!r}"
        )
    return cast(DataIntegrationFlowLoadType, data)
