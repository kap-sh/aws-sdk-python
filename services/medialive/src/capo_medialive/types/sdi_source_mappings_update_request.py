"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceMappingsUpdateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.sdi_source_mapping_update_request

SdiSourceMappingsUpdateRequest: TypeAlias = list[
    "capo_medialive.types.sdi_source_mapping_update_request.SdiSourceMappingUpdateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceMappingsUpdateRequest) -> list:
    import capo_medialive.types.sdi_source_mapping_update_request

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.sdi_source_mapping_update_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SdiSourceMappingsUpdateRequest:
    import capo_medialive.types.sdi_source_mapping_update_request

    out: SdiSourceMappingsUpdateRequest = []
    for item in data:
        out.append(
            capo_medialive.types.sdi_source_mapping_update_request.deserialize_json(
                item
            )
        )
    return out
