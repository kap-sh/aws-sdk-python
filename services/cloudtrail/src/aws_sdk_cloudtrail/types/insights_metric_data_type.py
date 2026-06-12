"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsightsMetricDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

InsightsMetricDataType: TypeAlias = Literal[
    "FillWithZeros",
    "NonZeroData",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FillWithZeros",
        "NonZeroData",
    )
)


def serialize_aws_json_1_1(value: InsightsMetricDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InsightsMetricDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightsMetricDataType value: {data!r}")
    return cast(InsightsMetricDataType, data)
