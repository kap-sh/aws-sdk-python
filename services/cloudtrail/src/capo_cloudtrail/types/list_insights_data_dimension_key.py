"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsDataDimensionKey``."""

from typing import Literal, TypeAlias, cast

ListInsightsDataDimensionKey: TypeAlias = Literal[
    "EventId",
    "EventName",
    "EventSource",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInsightsDataDimensionKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListInsightsDataDimensionKey:
    return cast(ListInsightsDataDimensionKey, data)
