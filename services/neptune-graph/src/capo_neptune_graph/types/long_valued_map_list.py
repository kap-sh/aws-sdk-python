"""Generated from Smithy shape ``com.amazonaws.neptunegraph#LongValuedMapList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptune_graph.types.long_valued_map

LongValuedMapList: TypeAlias = list[
    "capo_neptune_graph.types.long_valued_map.LongValuedMap"
]


# --- restJson1 ser/de ---
def serialize_json(value: LongValuedMapList) -> list:
    import capo_neptune_graph.types.long_valued_map

    out: list = []
    for item in value:
        out.append(capo_neptune_graph.types.long_valued_map.serialize_json(item))
    return out


def deserialize_json(data: list) -> LongValuedMapList:
    import capo_neptune_graph.types.long_valued_map

    out: LongValuedMapList = []
    for item in data:
        out.append(capo_neptune_graph.types.long_valued_map.deserialize_json(item))
    return out
