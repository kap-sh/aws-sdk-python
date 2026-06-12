"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfNodeInterfaceMappingCreateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.node_interface_mapping_create_request

__listOfNodeInterfaceMappingCreateRequest: TypeAlias = list[
    "aws_sdk_medialive.types.node_interface_mapping_create_request.NodeInterfaceMappingCreateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfNodeInterfaceMappingCreateRequest) -> list:
    import aws_sdk_medialive.types.node_interface_mapping_create_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.node_interface_mapping_create_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfNodeInterfaceMappingCreateRequest:
    import aws_sdk_medialive.types.node_interface_mapping_create_request

    out: __listOfNodeInterfaceMappingCreateRequest = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.node_interface_mapping_create_request.deserialize_json(
                item
            )
        )
    return out
