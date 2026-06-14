"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeNFSFileSharesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.nfs_file_share_info_list


class DescribeNFSFileSharesOutput(TypedDict):
    nfs_file_share_info_list: NotRequired[
        "aws_sdk_storage_gateway.types.nfs_file_share_info_list.NFSFileShareInfoList"
    ]
    """<p>An array containing a description for each requested file share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNFSFileSharesOutput) -> dict:
    out: dict = {}
    if "nfs_file_share_info_list" in value:
        import aws_sdk_storage_gateway.types.nfs_file_share_info_list

        out["NFSFileShareInfoList"] = (
            aws_sdk_storage_gateway.types.nfs_file_share_info_list.serialize_aws_json_1_1(
                value["nfs_file_share_info_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNFSFileSharesOutput:
    out: DescribeNFSFileSharesOutput = {}  # type: ignore[typeddict-item]
    if "NFSFileShareInfoList" in data:
        import aws_sdk_storage_gateway.types.nfs_file_share_info_list

        out["nfs_file_share_info_list"] = (
            aws_sdk_storage_gateway.types.nfs_file_share_info_list.deserialize_aws_json_1_1(
                data["NFSFileShareInfoList"]
            )
        )
    return out
