"""Generated from Smithy shape ``com.amazonaws.lambda#FileSystemConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.file_system_config

FileSystemConfigList: TypeAlias = list[
    "aws_sdk_lambda.types.file_system_config.FileSystemConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemConfigList) -> list:
    import aws_sdk_lambda.types.file_system_config

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.file_system_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> FileSystemConfigList:
    import aws_sdk_lambda.types.file_system_config

    out: FileSystemConfigList = []
    for item in data:
        out.append(aws_sdk_lambda.types.file_system_config.deserialize_json(item))
    return out
