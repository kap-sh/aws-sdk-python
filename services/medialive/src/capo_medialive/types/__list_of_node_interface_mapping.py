"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfNodeInterfaceMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.node_interface_mapping

__listOfNodeInterfaceMapping: TypeAlias = list[
    "capo_medialive.types.node_interface_mapping.NodeInterfaceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfNodeInterfaceMapping) -> list:
    import capo_medialive.types.node_interface_mapping

    out: list = []
    for item in value:
        out.append(capo_medialive.types.node_interface_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfNodeInterfaceMapping:
    import capo_medialive.types.node_interface_mapping

    out: __listOfNodeInterfaceMapping = []
    for item in data:
        out.append(capo_medialive.types.node_interface_mapping.deserialize_json(item))
    return out
