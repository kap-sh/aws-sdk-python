"""Generated from Smithy shape ``com.amazonaws.storagegateway#NFSFileShareInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.nfs_file_share_info

NFSFileShareInfoList: TypeAlias = list[
    "aws_sdk_storage_gateway.types.nfs_file_share_info.NFSFileShareInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NFSFileShareInfoList) -> list:
    import aws_sdk_storage_gateway.types.nfs_file_share_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.nfs_file_share_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NFSFileShareInfoList:
    import aws_sdk_storage_gateway.types.nfs_file_share_info

    out: NFSFileShareInfoList = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.nfs_file_share_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
