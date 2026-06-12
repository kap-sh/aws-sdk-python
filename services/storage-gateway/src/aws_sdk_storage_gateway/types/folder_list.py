"""Generated from Smithy shape ``com.amazonaws.storagegateway#FolderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.folder

FolderList: TypeAlias = list["aws_sdk_storage_gateway.types.folder.Folder"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FolderList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FolderList:
    return list(data)
