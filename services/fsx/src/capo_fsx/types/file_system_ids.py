"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.file_system_id

FileSystemIds: TypeAlias = list["capo_fsx.types.file_system_id.FileSystemId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FileSystemIds:
    return list(data)
