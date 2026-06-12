"""Generated from Smithy shape ``com.amazonaws.securityhub#FilePathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.file_paths

FilePathList: TypeAlias = list["aws_sdk_securityhub.types.file_paths.FilePaths"]


# --- restJson1 ser/de ---
def serialize_json(value: FilePathList) -> list:
    import aws_sdk_securityhub.types.file_paths

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.file_paths.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilePathList:
    import aws_sdk_securityhub.types.file_paths

    out: FilePathList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.file_paths.deserialize_json(item))
    return out
