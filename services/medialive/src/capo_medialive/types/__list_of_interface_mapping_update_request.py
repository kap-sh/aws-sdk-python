"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInterfaceMappingUpdateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.interface_mapping_update_request

__listOfInterfaceMappingUpdateRequest: TypeAlias = list[
    "capo_medialive.types.interface_mapping_update_request.InterfaceMappingUpdateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInterfaceMappingUpdateRequest) -> list:
    import capo_medialive.types.interface_mapping_update_request

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.interface_mapping_update_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfInterfaceMappingUpdateRequest:
    import capo_medialive.types.interface_mapping_update_request

    out: __listOfInterfaceMappingUpdateRequest = []
    for item in data:
        out.append(
            capo_medialive.types.interface_mapping_update_request.deserialize_json(item)
        )
    return out
