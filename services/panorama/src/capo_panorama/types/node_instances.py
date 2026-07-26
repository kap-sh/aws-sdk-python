"""Generated from Smithy shape ``com.amazonaws.panorama#NodeInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.node_instance

NodeInstances: TypeAlias = list["capo_panorama.types.node_instance.NodeInstance"]


# --- restJson1 ser/de ---
def serialize_json(value: NodeInstances) -> list:
    import capo_panorama.types.node_instance

    out: list = []
    for item in value:
        out.append(capo_panorama.types.node_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeInstances:
    import capo_panorama.types.node_instance

    out: NodeInstances = []
    for item in data:
        out.append(capo_panorama.types.node_instance.deserialize_json(item))
    return out
