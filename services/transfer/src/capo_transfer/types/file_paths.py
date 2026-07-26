"""Generated from Smithy shape ``com.amazonaws.transfer#FilePaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.file_path

FilePaths: TypeAlias = list["capo_transfer.types.file_path.FilePath"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilePaths) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilePaths:
    return list(data)
