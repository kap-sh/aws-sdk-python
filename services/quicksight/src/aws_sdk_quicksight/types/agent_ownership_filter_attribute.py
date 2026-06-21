"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentOwnershipFilterAttribute``."""

from typing import Literal, TypeAlias, cast

AgentOwnershipFilterAttribute: TypeAlias = Literal[
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "AGENT_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentOwnershipFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> AgentOwnershipFilterAttribute:
    return cast(AgentOwnershipFilterAttribute, data)
