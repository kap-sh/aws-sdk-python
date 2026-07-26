"""Generated from Smithy shape ``com.amazonaws.neptunedata#NodeStructures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptunedata.types.node_structure

NodeStructures: TypeAlias = list["capo_neptunedata.types.node_structure.NodeStructure"]


# --- restJson1 ser/de ---
def serialize_json(value: NodeStructures) -> list:
    import capo_neptunedata.types.node_structure

    out: list = []
    for item in value:
        out.append(capo_neptunedata.types.node_structure.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeStructures:
    import capo_neptunedata.types.node_structure

    out: NodeStructures = []
    for item in data:
        out.append(capo_neptunedata.types.node_structure.deserialize_json(item))
    return out
