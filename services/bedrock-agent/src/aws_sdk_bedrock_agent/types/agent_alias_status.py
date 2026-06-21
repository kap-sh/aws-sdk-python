"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasStatus``."""

from typing import Literal, TypeAlias, cast

AgentAliasStatus: TypeAlias = Literal[
    "CREATING",
    "PREPARED",
    "FAILED",
    "UPDATING",
    "DELETING",
    "DISSOCIATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentAliasStatus:
    return cast(AgentAliasStatus, data)
