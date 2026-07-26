"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.association

AssociationsList: TypeAlias = list["capo_devops_agent.types.association.Association"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationsList) -> list:
    import capo_devops_agent.types.association

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.association.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociationsList:
    import capo_devops_agent.types.association

    out: AssociationsList = []
    for item in data:
        out.append(capo_devops_agent.types.association.deserialize_json(item))
    return out
