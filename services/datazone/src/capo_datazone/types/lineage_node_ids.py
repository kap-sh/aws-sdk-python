"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.lineage_node_id

LineageNodeIds: TypeAlias = list["capo_datazone.types.lineage_node_id.LineageNodeId"]


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeIds) -> list:
    return list(value)


def deserialize_json(data: list) -> LineageNodeIds:
    return list(data)
