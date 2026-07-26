"""Generated from Smithy shape ``com.amazonaws.detective#GraphList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.graph

GraphList: TypeAlias = list["capo_detective.types.graph.Graph"]


# --- restJson1 ser/de ---
def serialize_json(value: GraphList) -> list:
    import capo_detective.types.graph

    out: list = []
    for item in value:
        out.append(capo_detective.types.graph.serialize_json(item))
    return out


def deserialize_json(data: list) -> GraphList:
    import capo_detective.types.graph

    out: GraphList = []
    for item in data:
        out.append(capo_detective.types.graph.deserialize_json(item))
    return out
