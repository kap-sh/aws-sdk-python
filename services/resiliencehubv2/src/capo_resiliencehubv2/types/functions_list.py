"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FunctionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.entity_id

FunctionsList: TypeAlias = list["capo_resiliencehubv2.types.entity_id.EntityId"]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> FunctionsList:
    return list(data)
