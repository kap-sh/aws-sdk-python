"""Generated from Smithy shape ``com.amazonaws.appflow#ExecutionIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.execution_id

ExecutionIds: TypeAlias = list["capo_appflow.types.execution_id.ExecutionId"]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ExecutionIds:
    return list(data)
