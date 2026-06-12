"""Generated from Smithy shape ``com.amazonaws.sagemaker#EventSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

EventSortBy: TypeAlias = Literal["EventTime",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EventTime",))


def serialize_aws_json_1_1(value: EventSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSortBy value: {data!r}")
    return cast(EventSortBy, data)
