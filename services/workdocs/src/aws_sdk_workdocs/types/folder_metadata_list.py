"""Generated from Smithy shape ``com.amazonaws.workdocs#FolderMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.folder_metadata

FolderMetadataList: TypeAlias = list[
    "aws_sdk_workdocs.types.folder_metadata.FolderMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderMetadataList) -> list:
    import aws_sdk_workdocs.types.folder_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.folder_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> FolderMetadataList:
    import aws_sdk_workdocs.types.folder_metadata

    out: FolderMetadataList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.folder_metadata.deserialize_json(item))
    return out
