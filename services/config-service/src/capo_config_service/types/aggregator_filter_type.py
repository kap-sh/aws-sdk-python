"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatorFilterType``."""

from typing import Literal, TypeAlias, cast

AggregatorFilterType: TypeAlias = Literal["INCLUDE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatorFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggregatorFilterType:
    return cast(AggregatorFilterType, data)
