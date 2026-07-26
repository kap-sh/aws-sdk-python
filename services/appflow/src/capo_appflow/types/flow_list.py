"""Generated from Smithy shape ``com.amazonaws.appflow#FlowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.flow_definition

FlowList: TypeAlias = list["capo_appflow.types.flow_definition.FlowDefinition"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowList) -> list:
    import capo_appflow.types.flow_definition

    out: list = []
    for item in value:
        out.append(capo_appflow.types.flow_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowList:
    import capo_appflow.types.flow_definition

    out: FlowList = []
    for item in data:
        out.append(capo_appflow.types.flow_definition.deserialize_json(item))
    return out
