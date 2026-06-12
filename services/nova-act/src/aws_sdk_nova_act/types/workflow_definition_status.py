"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_nova_act.errors import DeserializationError

WorkflowDefinitionStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
    )
)


def serialize_json(value: WorkflowDefinitionStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowDefinitionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowDefinitionStatus value: {data!r}")
    return cast(WorkflowDefinitionStatus, data)
