"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventCategoryAggregation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

EventCategoryAggregation: TypeAlias = Literal["Data",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Data",))


def serialize_aws_json_1_1(value: EventCategoryAggregation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventCategoryAggregation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventCategoryAggregation value: {data!r}")
    return cast(EventCategoryAggregation, data)
