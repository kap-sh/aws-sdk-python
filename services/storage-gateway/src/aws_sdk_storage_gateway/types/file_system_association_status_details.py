"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileSystemAssociationStatusDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_status_detail

FileSystemAssociationStatusDetails: TypeAlias = list[
    "aws_sdk_storage_gateway.types.file_system_association_status_detail.FileSystemAssociationStatusDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemAssociationStatusDetails) -> list:
    import aws_sdk_storage_gateway.types.file_system_association_status_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.file_system_association_status_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FileSystemAssociationStatusDetails:
    import aws_sdk_storage_gateway.types.file_system_association_status_detail

    out: FileSystemAssociationStatusDetails = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.file_system_association_status_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
