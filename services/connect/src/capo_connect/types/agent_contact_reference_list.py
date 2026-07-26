"""Generated from Smithy shape ``com.amazonaws.connect#AgentContactReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.agent_contact_reference

AgentContactReferenceList: TypeAlias = list[
    "capo_connect.types.agent_contact_reference.AgentContactReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentContactReferenceList) -> list:
    import capo_connect.types.agent_contact_reference

    out: list = []
    for item in value:
        out.append(capo_connect.types.agent_contact_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentContactReferenceList:
    import capo_connect.types.agent_contact_reference

    out: AgentContactReferenceList = []
    for item in data:
        out.append(capo_connect.types.agent_contact_reference.deserialize_json(item))
    return out
