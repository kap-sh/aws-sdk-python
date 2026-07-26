"""Generated from Smithy shape ``com.amazonaws.glacier#UploadsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glacier.types.upload_list_element

UploadsList: TypeAlias = list[
    "capo_glacier.types.upload_list_element.UploadListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: UploadsList) -> list:
    import capo_glacier.types.upload_list_element

    out: list = []
    for item in value:
        out.append(capo_glacier.types.upload_list_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> UploadsList:
    import capo_glacier.types.upload_list_element

    out: UploadsList = []
    for item in data:
        out.append(capo_glacier.types.upload_list_element.deserialize_json(item))
    return out
