"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceMappingsUpdateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.sdi_source_mapping_update_request

SdiSourceMappingsUpdateRequest: TypeAlias = list[
    "aws_sdk_medialive.types.sdi_source_mapping_update_request.SdiSourceMappingUpdateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceMappingsUpdateRequest) -> list:
    import aws_sdk_medialive.types.sdi_source_mapping_update_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.sdi_source_mapping_update_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SdiSourceMappingsUpdateRequest:
    import aws_sdk_medialive.types.sdi_source_mapping_update_request

    out: SdiSourceMappingsUpdateRequest = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.sdi_source_mapping_update_request.deserialize_json(
                item
            )
        )
    return out
