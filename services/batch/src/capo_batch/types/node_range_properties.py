"""Generated from Smithy shape ``com.amazonaws.batch#NodeRangeProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.node_range_property

NodeRangeProperties: TypeAlias = list[
    "capo_batch.types.node_range_property.NodeRangeProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeRangeProperties) -> list:
    import capo_batch.types.node_range_property

    out: list = []
    for item in value:
        out.append(capo_batch.types.node_range_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeRangeProperties:
    import capo_batch.types.node_range_property

    out: NodeRangeProperties = []
    for item in data:
        out.append(capo_batch.types.node_range_property.deserialize_json(item))
    return out
