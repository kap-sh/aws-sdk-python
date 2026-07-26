"""Generated from Smithy shape ``com.amazonaws.codecommit#FilesMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.file_metadata

FilesMetadata: TypeAlias = list["capo_codecommit.types.file_metadata.FileMetadata"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilesMetadata) -> list:
    import capo_codecommit.types.file_metadata

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.file_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilesMetadata:
    import capo_codecommit.types.file_metadata

    out: FilesMetadata = []
    for item in data:
        out.append(capo_codecommit.types.file_metadata.deserialize_aws_json_1_1(item))
    return out
