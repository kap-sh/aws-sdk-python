"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#MetricsLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

MetricsLevel: TypeAlias = Literal[
    "APPLICATION",
    "TASK",
    "OPERATOR",
    "PARALLELISM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLICATION",
        "TASK",
        "OPERATOR",
        "PARALLELISM",
    )
)


def serialize_aws_json_1_1(value: MetricsLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricsLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricsLevel value: {data!r}")
    return cast(MetricsLevel, data)
