"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowDefinitionStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowDefinitionStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowDefinitionStatus:
    return cast(WorkflowDefinitionStatus, data)
