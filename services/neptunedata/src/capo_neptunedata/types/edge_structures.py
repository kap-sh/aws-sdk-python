"""Generated from Smithy shape ``com.amazonaws.neptunedata#EdgeStructures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptunedata.types.edge_structure

EdgeStructures: TypeAlias = list["capo_neptunedata.types.edge_structure.EdgeStructure"]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeStructures) -> list:
    import capo_neptunedata.types.edge_structure

    out: list = []
    for item in value:
        out.append(capo_neptunedata.types.edge_structure.serialize_json(item))
    return out


def deserialize_json(data: list) -> EdgeStructures:
    import capo_neptunedata.types.edge_structure

    out: EdgeStructures = []
    for item in data:
        out.append(capo_neptunedata.types.edge_structure.deserialize_json(item))
    return out
