"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeNFSFileSharesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.nfs_file_share_info_list


class DescribeNFSFileSharesOutput(TypedDict, closed=True):
    nfs_file_share_info_list: NotRequired[
        "capo_storage_gateway.types.nfs_file_share_info_list.NFSFileShareInfoList"
    ]
    """<p>An array containing a description for each requested file share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNFSFileSharesOutput) -> dict:
    out: dict = {}
    if "nfs_file_share_info_list" in value:
        import capo_storage_gateway.types.nfs_file_share_info_list

        out["NFSFileShareInfoList"] = (
            capo_storage_gateway.types.nfs_file_share_info_list.serialize_aws_json_1_1(
                value["nfs_file_share_info_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNFSFileSharesOutput:
    out: DescribeNFSFileSharesOutput = {}  # type: ignore[typeddict-item]
    if "NFSFileShareInfoList" in data:
        import capo_storage_gateway.types.nfs_file_share_info_list

        out["nfs_file_share_info_list"] = (
            capo_storage_gateway.types.nfs_file_share_info_list.deserialize_aws_json_1_1(
                data["NFSFileShareInfoList"]
            )
        )
    return out
