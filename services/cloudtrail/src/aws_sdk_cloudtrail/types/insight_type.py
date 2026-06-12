"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsightType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

InsightType: TypeAlias = Literal[
    "ApiCallRateInsight",
    "ApiErrorRateInsight",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ApiCallRateInsight",
        "ApiErrorRateInsight",
    )
)


def serialize_aws_json_1_1(value: InsightType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InsightType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightType value: {data!r}")
    return cast(InsightType, data)
