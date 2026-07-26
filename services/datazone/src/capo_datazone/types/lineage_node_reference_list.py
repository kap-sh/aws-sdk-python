"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.lineage_node_reference

LineageNodeReferenceList: TypeAlias = list[
    "capo_datazone.types.lineage_node_reference.LineageNodeReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeReferenceList) -> list:
    import capo_datazone.types.lineage_node_reference

    out: list = []
    for item in value:
        out.append(capo_datazone.types.lineage_node_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineageNodeReferenceList:
    import capo_datazone.types.lineage_node_reference

    out: LineageNodeReferenceList = []
    for item in data:
        out.append(capo_datazone.types.lineage_node_reference.deserialize_json(item))
    return out
