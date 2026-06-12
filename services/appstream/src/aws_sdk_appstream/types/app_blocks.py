"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.app_block

AppBlocks: TypeAlias = list["aws_sdk_appstream.types.app_block.AppBlock"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlocks) -> list:
    import aws_sdk_appstream.types.app_block

    out: list = []
    for item in value:
        out.append(aws_sdk_appstream.types.app_block.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppBlocks:
    import aws_sdk_appstream.types.app_block

    out: AppBlocks = []
    for item in data:
        out.append(aws_sdk_appstream.types.app_block.deserialize_aws_json_1_1(item))
    return out
