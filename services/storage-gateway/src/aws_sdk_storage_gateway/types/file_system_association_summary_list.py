"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileSystemAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_summary

FileSystemAssociationSummaryList: TypeAlias = list[
    "aws_sdk_storage_gateway.types.file_system_association_summary.FileSystemAssociationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemAssociationSummaryList) -> list:
    import aws_sdk_storage_gateway.types.file_system_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.file_system_association_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FileSystemAssociationSummaryList:
    import aws_sdk_storage_gateway.types.file_system_association_summary

    out: FileSystemAssociationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.file_system_association_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
