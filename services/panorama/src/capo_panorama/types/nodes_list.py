"""Generated from Smithy shape ``com.amazonaws.panorama#NodesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.node

NodesList: TypeAlias = list["capo_panorama.types.node.Node"]


# --- restJson1 ser/de ---
def serialize_json(value: NodesList) -> list:
    import capo_panorama.types.node

    out: list = []
    for item in value:
        out.append(capo_panorama.types.node.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodesList:
    import capo_panorama.types.node

    out: NodesList = []
    for item in data:
        out.append(capo_panorama.types.node.deserialize_json(item))
    return out
