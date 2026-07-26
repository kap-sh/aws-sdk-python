"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInterfaceMappingCreateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.interface_mapping_create_request

__listOfInterfaceMappingCreateRequest: TypeAlias = list[
    "capo_medialive.types.interface_mapping_create_request.InterfaceMappingCreateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInterfaceMappingCreateRequest) -> list:
    import capo_medialive.types.interface_mapping_create_request

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.interface_mapping_create_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfInterfaceMappingCreateRequest:
    import capo_medialive.types.interface_mapping_create_request

    out: __listOfInterfaceMappingCreateRequest = []
    for item in data:
        out.append(
            capo_medialive.types.interface_mapping_create_request.deserialize_json(item)
        )
    return out
