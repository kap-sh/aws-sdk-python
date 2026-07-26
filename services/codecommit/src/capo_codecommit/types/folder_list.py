"""Generated from Smithy shape ``com.amazonaws.codecommit#FolderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.folder

FolderList: TypeAlias = list["capo_codecommit.types.folder.Folder"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FolderList) -> list:
    import capo_codecommit.types.folder

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.folder.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FolderList:
    import capo_codecommit.types.folder

    out: FolderList = []
    for item in data:
        out.append(capo_codecommit.types.folder.deserialize_aws_json_1_1(item))
    return out
