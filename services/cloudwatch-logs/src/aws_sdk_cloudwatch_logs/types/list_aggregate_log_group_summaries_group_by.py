"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListAggregateLogGroupSummariesGroupBy``."""

from typing import Literal, TypeAlias, cast

ListAggregateLogGroupSummariesGroupBy: TypeAlias = Literal[
    "DATA_SOURCE_NAME_TYPE_AND_FORMAT",
    "DATA_SOURCE_NAME_AND_TYPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAggregateLogGroupSummariesGroupBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListAggregateLogGroupSummariesGroupBy:
    return cast(ListAggregateLogGroupSummariesGroupBy, data)
