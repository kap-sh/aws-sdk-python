"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEdgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.dataflow_edge

DataflowEdgeList: TypeAlias = list[
    "capo_groundstation.types.dataflow_edge.DataflowEdge"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEdgeList) -> list:
    import capo_groundstation.types.dataflow_edge

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.dataflow_edge.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataflowEdgeList:
    import capo_groundstation.types.dataflow_edge

    out: DataflowEdgeList = []
    for item in data:
        out.append(capo_groundstation.types.dataflow_edge.deserialize_json(item))
    return out
