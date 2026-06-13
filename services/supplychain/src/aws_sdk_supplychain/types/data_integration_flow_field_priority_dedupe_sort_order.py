"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowFieldPriorityDedupeSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataIntegrationFlowFieldPriorityDedupeSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: DataIntegrationFlowFieldPriorityDedupeSortOrder) -> str:
    return value


def deserialize_json(data: str) -> DataIntegrationFlowFieldPriorityDedupeSortOrder:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataIntegrationFlowFieldPriorityDedupeSortOrder value: {data!r}"
        )
    return cast(DataIntegrationFlowFieldPriorityDedupeSortOrder, data)
