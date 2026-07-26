"""Generated from Smithy shape ``com.amazonaws.workdocs#FolderMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.folder_metadata

FolderMetadataList: TypeAlias = list[
    "capo_workdocs.types.folder_metadata.FolderMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderMetadataList) -> list:
    import capo_workdocs.types.folder_metadata

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.folder_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> FolderMetadataList:
    import capo_workdocs.types.folder_metadata

    out: FolderMetadataList = []
    for item in data:
        out.append(capo_workdocs.types.folder_metadata.deserialize_json(item))
    return out
