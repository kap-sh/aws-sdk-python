"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsDataDimensionKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

ListInsightsDataDimensionKey: TypeAlias = Literal[
    "EventId",
    "EventName",
    "EventSource",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EventId",
        "EventName",
        "EventSource",
    )
)


def serialize_aws_json_1_1(value: ListInsightsDataDimensionKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListInsightsDataDimensionKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListInsightsDataDimensionKey value: {data!r}"
        )
    return cast(ListInsightsDataDimensionKey, data)
