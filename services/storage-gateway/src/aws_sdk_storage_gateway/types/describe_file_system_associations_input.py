"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeFileSystemAssociationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_arn_list


class DescribeFileSystemAssociationsInput(TypedDict):
    file_system_association_arn_list: "aws_sdk_storage_gateway.types.file_system_association_arn_list.FileSystemAssociationARNList"
    """<p>An array containing the Amazon Resource Name (ARN) of each file system association to be described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemAssociationsInput) -> dict:
    out: dict = {}
    import aws_sdk_storage_gateway.types.file_system_association_arn_list

    out["FileSystemAssociationARNList"] = (
        aws_sdk_storage_gateway.types.file_system_association_arn_list.serialize_aws_json_1_1(
            value["file_system_association_arn_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemAssociationsInput:
    out: DescribeFileSystemAssociationsInput = {}  # type: ignore[typeddict-item]
    if "FileSystemAssociationARNList" in data:
        import aws_sdk_storage_gateway.types.file_system_association_arn_list

        out["file_system_association_arn_list"] = (
            aws_sdk_storage_gateway.types.file_system_association_arn_list.deserialize_aws_json_1_1(
                data["FileSystemAssociationARNList"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeFileSystemAssociationsInput.file_system_association_arn_list required"
        )
    return out
