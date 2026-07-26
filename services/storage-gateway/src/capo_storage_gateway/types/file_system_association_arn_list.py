"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileSystemAssociationARNList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_system_association_arn

FileSystemAssociationARNList: TypeAlias = list[
    "capo_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemAssociationARNList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FileSystemAssociationARNList:
    return list(data)
