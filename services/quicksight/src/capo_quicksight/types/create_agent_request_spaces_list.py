"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAgentRequestSpacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

CreateAgentRequestSpacesList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentRequestSpacesList) -> list:
    return list(value)


def deserialize_json(data: list) -> CreateAgentRequestSpacesList:
    return list(data)
