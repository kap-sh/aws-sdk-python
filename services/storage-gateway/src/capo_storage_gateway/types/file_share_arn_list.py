"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileShareARNList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_share_arn

FileShareARNList: TypeAlias = list[
    "capo_storage_gateway.types.file_share_arn.FileShareARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileShareARNList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FileShareARNList:
    return list(data)
