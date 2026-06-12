"""Generated from Smithy shape ``com.amazonaws.kendra#FolderIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.folder_id

FolderIdList: TypeAlias = list["aws_sdk_kendra.types.folder_id.FolderId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FolderIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FolderIdList:
    return list(data)
