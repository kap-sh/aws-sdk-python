"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventCategoryAggregation``."""

from typing import Literal, TypeAlias, cast

EventCategoryAggregation: TypeAlias = Literal["Data",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventCategoryAggregation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventCategoryAggregation:
    return cast(EventCategoryAggregation, data)
