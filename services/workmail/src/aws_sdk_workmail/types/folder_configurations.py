"""Generated from Smithy shape ``com.amazonaws.workmail#FolderConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.folder_configuration

FolderConfigurations: TypeAlias = list[
    "aws_sdk_workmail.types.folder_configuration.FolderConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FolderConfigurations) -> list:
    import aws_sdk_workmail.types.folder_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workmail.types.folder_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FolderConfigurations:
    import aws_sdk_workmail.types.folder_configuration

    out: FolderConfigurations = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.folder_configuration.deserialize_aws_json_1_1(item)
        )
    return out
