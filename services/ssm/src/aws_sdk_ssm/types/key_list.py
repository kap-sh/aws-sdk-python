"""Generated from Smithy shape ``com.amazonaws.ssm#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.tag_key

KeyList: TypeAlias = list["aws_sdk_ssm.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> KeyList:
    return list(data)
