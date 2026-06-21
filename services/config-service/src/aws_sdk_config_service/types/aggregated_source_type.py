"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatedSourceType``."""

from typing import Literal, TypeAlias, cast

AggregatedSourceType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggregatedSourceType:
    return cast(AggregatedSourceType, data)
