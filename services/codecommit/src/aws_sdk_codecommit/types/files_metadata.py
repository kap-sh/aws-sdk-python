"""Generated from Smithy shape ``com.amazonaws.codecommit#FilesMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.file_metadata

FilesMetadata: TypeAlias = list["aws_sdk_codecommit.types.file_metadata.FileMetadata"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilesMetadata) -> list:
    import aws_sdk_codecommit.types.file_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.file_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilesMetadata:
    import aws_sdk_codecommit.types.file_metadata

    out: FilesMetadata = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.file_metadata.deserialize_aws_json_1_1(item)
        )
    return out
