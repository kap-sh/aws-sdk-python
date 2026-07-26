"""Generated from Smithy shape ``com.amazonaws.batch#NodePropertyOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.node_property_override

NodePropertyOverrides: TypeAlias = list[
    "capo_batch.types.node_property_override.NodePropertyOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodePropertyOverrides) -> list:
    import capo_batch.types.node_property_override

    out: list = []
    for item in value:
        out.append(capo_batch.types.node_property_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodePropertyOverrides:
    import capo_batch.types.node_property_override

    out: NodePropertyOverrides = []
    for item in data:
        out.append(capo_batch.types.node_property_override.deserialize_json(item))
    return out
