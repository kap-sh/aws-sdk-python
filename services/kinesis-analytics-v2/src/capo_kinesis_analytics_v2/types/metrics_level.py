"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#MetricsLevel``."""

from typing import Literal, TypeAlias, cast

MetricsLevel: TypeAlias = Literal[
    "APPLICATION",
    "TASK",
    "OPERATOR",
    "PARALLELISM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricsLevel:
    return cast(MetricsLevel, data)
