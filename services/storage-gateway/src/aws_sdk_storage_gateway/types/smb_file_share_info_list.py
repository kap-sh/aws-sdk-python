"""Generated from Smithy shape ``com.amazonaws.storagegateway#SMBFileShareInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.smb_file_share_info

SMBFileShareInfoList: TypeAlias = list[
    "aws_sdk_storage_gateway.types.smb_file_share_info.SMBFileShareInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SMBFileShareInfoList) -> list:
    import aws_sdk_storage_gateway.types.smb_file_share_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.smb_file_share_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SMBFileShareInfoList:
    import aws_sdk_storage_gateway.types.smb_file_share_info

    out: SMBFileShareInfoList = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.smb_file_share_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
