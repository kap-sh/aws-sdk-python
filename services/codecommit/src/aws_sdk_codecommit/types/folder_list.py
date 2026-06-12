"""Generated from Smithy shape ``com.amazonaws.codecommit#FolderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.folder

FolderList: TypeAlias = list["aws_sdk_codecommit.types.folder.Folder"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FolderList) -> list:
    import aws_sdk_codecommit.types.folder

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.folder.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FolderList:
    import aws_sdk_codecommit.types.folder

    out: FolderList = []
    for item in data:
        out.append(aws_sdk_codecommit.types.folder.deserialize_aws_json_1_1(item))
    return out
