"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeFileSystemAssociationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_info_list


class DescribeFileSystemAssociationsOutput(TypedDict):
    file_system_association_info_list: NotRequired[
        "aws_sdk_storage_gateway.types.file_system_association_info_list.FileSystemAssociationInfoList"
    ]
    """<p>An array containing the <code>FileSystemAssociationInfo</code> data type of each file system association to be described. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemAssociationsOutput) -> dict:
    out: dict = {}
    if "file_system_association_info_list" in value:
        import aws_sdk_storage_gateway.types.file_system_association_info_list

        out["FileSystemAssociationInfoList"] = (
            aws_sdk_storage_gateway.types.file_system_association_info_list.serialize_aws_json_1_1(
                value["file_system_association_info_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemAssociationsOutput:
    out: DescribeFileSystemAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "FileSystemAssociationInfoList" in data:
        import aws_sdk_storage_gateway.types.file_system_association_info_list

        out["file_system_association_info_list"] = (
            aws_sdk_storage_gateway.types.file_system_association_info_list.deserialize_aws_json_1_1(
                data["FileSystemAssociationInfoList"]
            )
        )
    return out
