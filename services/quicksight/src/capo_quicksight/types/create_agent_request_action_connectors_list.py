"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAgentRequestActionConnectorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

CreateAgentRequestActionConnectorsList: TypeAlias = list[
    "capo_quicksight.types.arn.Arn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentRequestActionConnectorsList) -> list:
    return list(value)


def deserialize_json(data: list) -> CreateAgentRequestActionConnectorsList:
    return list(data)
