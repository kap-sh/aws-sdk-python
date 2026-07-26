"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentRequestSpacesToAddList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

UpdateAgentRequestSpacesToAddList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRequestSpacesToAddList) -> list:
    return list(value)


def deserialize_json(data: list) -> UpdateAgentRequestSpacesToAddList:
    return list(data)
