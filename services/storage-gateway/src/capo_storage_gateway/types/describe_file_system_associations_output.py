"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeFileSystemAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_system_association_info_list


class DescribeFileSystemAssociationsOutput(TypedDict, closed=True):
    file_system_association_info_list: NotRequired[
        "capo_storage_gateway.types.file_system_association_info_list.FileSystemAssociationInfoList"
    ]
    """<p>An array containing the <code>FileSystemAssociationInfo</code> data type of each file system association to be described. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemAssociationsOutput) -> dict:
    out: dict = {}
    if "file_system_association_info_list" in value:
        import capo_storage_gateway.types.file_system_association_info_list

        out["FileSystemAssociationInfoList"] = (
            capo_storage_gateway.types.file_system_association_info_list.serialize_aws_json_1_1(
                value["file_system_association_info_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemAssociationsOutput:
    out: DescribeFileSystemAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "FileSystemAssociationInfoList" in data:
        import capo_storage_gateway.types.file_system_association_info_list

        out["file_system_association_info_list"] = (
            capo_storage_gateway.types.file_system_association_info_list.deserialize_aws_json_1_1(
                data["FileSystemAssociationInfoList"]
            )
        )
    return out
