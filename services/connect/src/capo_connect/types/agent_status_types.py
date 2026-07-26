"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.agent_status_type

AgentStatusTypes: TypeAlias = list[
    "capo_connect.types.agent_status_type.AgentStatusType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusTypes) -> list:
    import capo_connect.types.agent_status_type

    out: list = []
    for item in value:
        out.append(capo_connect.types.agent_status_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentStatusTypes:
    import capo_connect.types.agent_status_type

    out: AgentStatusTypes = []
    for item in data:
        out.append(capo_connect.types.agent_status_type.deserialize_json(item))
    return out
