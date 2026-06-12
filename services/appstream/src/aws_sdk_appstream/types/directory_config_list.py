"""Generated from Smithy shape ``com.amazonaws.appstream#DirectoryConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.directory_config

DirectoryConfigList: TypeAlias = list[
    "aws_sdk_appstream.types.directory_config.DirectoryConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryConfigList) -> list:
    import aws_sdk_appstream.types.directory_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.directory_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DirectoryConfigList:
    import aws_sdk_appstream.types.directory_config

    out: DirectoryConfigList = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.directory_config.deserialize_aws_json_1_1(item)
        )
    return out
