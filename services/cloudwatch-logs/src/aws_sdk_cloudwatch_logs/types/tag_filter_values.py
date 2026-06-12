"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TagFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.tag_filter_value

TagFilterValues: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.tag_filter_value.TagFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagFilterValues:
    return list(data)
