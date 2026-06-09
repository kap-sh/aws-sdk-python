"""Generated from Smithy shape ``com.amazonaws.secretsmanager#TagListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.tag

TagListType: TypeAlias = list["aws_sdk_secrets_manager.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagListType) -> list:
    import aws_sdk_secrets_manager.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_secrets_manager.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagListType:
    import aws_sdk_secrets_manager.types.tag

    out: TagListType = []
    for item in data:
        out.append(aws_sdk_secrets_manager.types.tag.deserialize_aws_json_1_1(item))
    return out
