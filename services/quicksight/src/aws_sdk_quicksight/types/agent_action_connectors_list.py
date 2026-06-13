"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentActionConnectorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn

AgentActionConnectorsList: TypeAlias = list["aws_sdk_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentActionConnectorsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentActionConnectorsList:
    return list(data)
