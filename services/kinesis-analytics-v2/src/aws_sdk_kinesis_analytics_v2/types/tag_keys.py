"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.tag_key

TagKeys: TypeAlias = list["aws_sdk_kinesis_analytics_v2.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagKeys:
    return list(data)
