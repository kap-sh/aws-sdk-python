"""Generated from Smithy shape ``com.amazonaws.secretsmanager#TagKeyListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.tag_key_type

TagKeyListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.tag_key_type.TagKeyType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeyListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeyListType:
    return list(data)
