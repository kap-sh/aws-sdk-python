"""Generated from Smithy shape ``com.amazonaws.panorama#InputPortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.node_input_port

InputPortList: TypeAlias = list["capo_panorama.types.node_input_port.NodeInputPort"]


# --- restJson1 ser/de ---
def serialize_json(value: InputPortList) -> list:
    import capo_panorama.types.node_input_port

    out: list = []
    for item in value:
        out.append(capo_panorama.types.node_input_port.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputPortList:
    import capo_panorama.types.node_input_port

    out: InputPortList = []
    for item in data:
        out.append(capo_panorama.types.node_input_port.deserialize_json(item))
    return out
