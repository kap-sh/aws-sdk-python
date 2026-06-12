"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileSystemAssociationInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_info

FileSystemAssociationInfoList: TypeAlias = list[
    "aws_sdk_storage_gateway.types.file_system_association_info.FileSystemAssociationInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemAssociationInfoList) -> list:
    import aws_sdk_storage_gateway.types.file_system_association_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.file_system_association_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FileSystemAssociationInfoList:
    import aws_sdk_storage_gateway.types.file_system_association_info

    out: FileSystemAssociationInfoList = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.file_system_association_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
