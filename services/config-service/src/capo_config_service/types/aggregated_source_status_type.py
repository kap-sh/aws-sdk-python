"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatedSourceStatusType``."""

from typing import Literal, TypeAlias, cast

AggregatedSourceStatusType: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "OUTDATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedSourceStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggregatedSourceStatusType:
    return cast(AggregatedSourceStatusType, data)
