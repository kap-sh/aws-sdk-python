"""Generated from Smithy shape ``com.amazonaws.sagemaker#EventSortBy``."""

from typing import Literal, TypeAlias, cast

EventSortBy: TypeAlias = Literal["EventTime",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventSortBy:
    return cast(EventSortBy, data)
