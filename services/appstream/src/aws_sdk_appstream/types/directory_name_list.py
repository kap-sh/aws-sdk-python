"""Generated from Smithy shape ``com.amazonaws.appstream#DirectoryNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.directory_name

DirectoryNameList: TypeAlias = list[
    "aws_sdk_appstream.types.directory_name.DirectoryName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DirectoryNameList:
    return list(data)
