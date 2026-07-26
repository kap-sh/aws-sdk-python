"""Generated from Smithy shape ``com.amazonaws.codepipeline#FilePathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.file_path

FilePathList: TypeAlias = list["capo_codepipeline.types.file_path.FilePath"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilePathList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilePathList:
    return list(data)
