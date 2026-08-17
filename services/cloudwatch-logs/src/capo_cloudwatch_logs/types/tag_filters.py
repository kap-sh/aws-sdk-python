"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TagFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.tag_filter

TagFilters: TypeAlias = list["capo_cloudwatch_logs.types.tag_filter.TagFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilters) -> list:
    import capo_cloudwatch_logs.types.tag_filter

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.tag_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagFilters:
    import capo_cloudwatch_logs.types.tag_filter

    out: TagFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch_logs.types.tag_filter.deserialize_aws_json_1_1(item))
    return out
