"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

PolicyType: TypeAlias = Literal[
    "DATA_PROTECTION_POLICY",
    "SUBSCRIPTION_FILTER_POLICY",
    "FIELD_INDEX_POLICY",
    "TRANSFORMER_POLICY",
    "METRIC_EXTRACTION_POLICY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATA_PROTECTION_POLICY",
        "SUBSCRIPTION_FILTER_POLICY",
        "FIELD_INDEX_POLICY",
        "TRANSFORMER_POLICY",
        "METRIC_EXTRACTION_POLICY",
    )
)


def serialize_aws_json_1_1(value: PolicyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyType value: {data!r}")
    return cast(PolicyType, data)
