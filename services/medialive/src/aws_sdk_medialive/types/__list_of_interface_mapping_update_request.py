"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInterfaceMappingUpdateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.interface_mapping_update_request

__listOfInterfaceMappingUpdateRequest: TypeAlias = list[
    "aws_sdk_medialive.types.interface_mapping_update_request.InterfaceMappingUpdateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInterfaceMappingUpdateRequest) -> list:
    import aws_sdk_medialive.types.interface_mapping_update_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.interface_mapping_update_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfInterfaceMappingUpdateRequest:
    import aws_sdk_medialive.types.interface_mapping_update_request

    out: __listOfInterfaceMappingUpdateRequest = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.interface_mapping_update_request.deserialize_json(
                item
            )
        )
    return out
