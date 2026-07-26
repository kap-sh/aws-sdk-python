"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentRequestSpacesToRemoveList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

UpdateAgentRequestSpacesToRemoveList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRequestSpacesToRemoveList) -> list:
    return list(value)


def deserialize_json(data: list) -> UpdateAgentRequestSpacesToRemoveList:
    return list(data)
