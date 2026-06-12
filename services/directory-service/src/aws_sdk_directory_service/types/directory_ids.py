"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id

DirectoryIds: TypeAlias = list[
    "aws_sdk_directory_service.types.directory_id.DirectoryId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DirectoryIds:
    return list(data)
