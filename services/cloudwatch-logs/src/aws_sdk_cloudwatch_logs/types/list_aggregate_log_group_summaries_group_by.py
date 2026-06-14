"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListAggregateLogGroupSummariesGroupBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

ListAggregateLogGroupSummariesGroupBy: TypeAlias = Literal[
    "DATA_SOURCE_NAME_TYPE_AND_FORMAT",
    "DATA_SOURCE_NAME_AND_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATA_SOURCE_NAME_TYPE_AND_FORMAT",
        "DATA_SOURCE_NAME_AND_TYPE",
    )
)


def serialize_aws_json_1_1(value: ListAggregateLogGroupSummariesGroupBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListAggregateLogGroupSummariesGroupBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListAggregateLogGroupSummariesGroupBy value: {data!r}"
        )
    return cast(ListAggregateLogGroupSummariesGroupBy, data)
