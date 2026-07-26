"""Generated from Smithy shape ``com.amazonaws.detective#UnprocessedGraphList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.unprocessed_graph

UnprocessedGraphList: TypeAlias = list[
    "capo_detective.types.unprocessed_graph.UnprocessedGraph"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedGraphList) -> list:
    import capo_detective.types.unprocessed_graph

    out: list = []
    for item in value:
        out.append(capo_detective.types.unprocessed_graph.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnprocessedGraphList:
    import capo_detective.types.unprocessed_graph

    out: UnprocessedGraphList = []
    for item in data:
        out.append(capo_detective.types.unprocessed_graph.deserialize_json(item))
    return out
