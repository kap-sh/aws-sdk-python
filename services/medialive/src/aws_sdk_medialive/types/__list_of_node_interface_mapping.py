"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfNodeInterfaceMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.node_interface_mapping

__listOfNodeInterfaceMapping: TypeAlias = list[
    "aws_sdk_medialive.types.node_interface_mapping.NodeInterfaceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfNodeInterfaceMapping) -> list:
    import aws_sdk_medialive.types.node_interface_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.node_interface_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfNodeInterfaceMapping:
    import aws_sdk_medialive.types.node_interface_mapping

    out: __listOfNodeInterfaceMapping = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.node_interface_mapping.deserialize_json(item)
        )
    return out
