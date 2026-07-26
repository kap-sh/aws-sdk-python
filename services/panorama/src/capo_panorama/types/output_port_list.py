"""Generated from Smithy shape ``com.amazonaws.panorama#OutputPortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.node_output_port

OutputPortList: TypeAlias = list["capo_panorama.types.node_output_port.NodeOutputPort"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputPortList) -> list:
    import capo_panorama.types.node_output_port

    out: list = []
    for item in value:
        out.append(capo_panorama.types.node_output_port.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputPortList:
    import capo_panorama.types.node_output_port

    out: OutputPortList = []
    for item in data:
        out.append(capo_panorama.types.node_output_port.deserialize_json(item))
    return out
