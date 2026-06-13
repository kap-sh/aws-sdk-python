"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.association

AssociationsList: TypeAlias = list["aws_sdk_devops_agent.types.association.Association"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationsList) -> list:
    import aws_sdk_devops_agent.types.association

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.association.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociationsList:
    import aws_sdk_devops_agent.types.association

    out: AssociationsList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.association.deserialize_json(item))
    return out
