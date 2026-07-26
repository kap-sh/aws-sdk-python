"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentSpacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

AgentSpacesList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpacesList) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentSpacesList:
    return list(data)
