"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsDataType``."""

from typing import Literal, TypeAlias, cast

ListInsightsDataType: TypeAlias = Literal["InsightsEvents",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInsightsDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListInsightsDataType:
    return cast(ListInsightsDataType, data)
