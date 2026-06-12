"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.tag_key

TagList: TypeAlias = list["aws_sdk_cloudwatch_logs.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagList:
    return list(data)
