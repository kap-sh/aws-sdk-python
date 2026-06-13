"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationFlowExecutionStatus: TypeAlias = Literal[
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


def serialize_json(value: DataIntegrationFlowExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationFlowExecutionStatus value: {data!r}"
        )
    return cast(DataIntegrationFlowExecutionStatus, data)
