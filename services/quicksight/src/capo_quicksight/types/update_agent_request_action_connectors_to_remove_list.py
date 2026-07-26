"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentRequestActionConnectorsToRemoveList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

UpdateAgentRequestActionConnectorsToRemoveList: TypeAlias = list[
    "capo_quicksight.types.arn.Arn"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRequestActionConnectorsToRemoveList) -> list:
    return list(value)


def deserialize_json(data: list) -> UpdateAgentRequestActionConnectorsToRemoveList:
    return list(data)
