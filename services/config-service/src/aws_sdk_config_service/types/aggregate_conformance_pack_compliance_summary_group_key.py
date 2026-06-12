"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateConformancePackComplianceSummaryGroupKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

AggregateConformancePackComplianceSummaryGroupKey: TypeAlias = Literal[
    "ACCOUNT_ID",
    "AWS_REGION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_ID",
        "AWS_REGION",
    )
)


def serialize_aws_json_1_1(
    value: AggregateConformancePackComplianceSummaryGroupKey,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> AggregateConformancePackComplianceSummaryGroupKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AggregateConformancePackComplianceSummaryGroupKey value: {data!r}"
        )
    return cast(AggregateConformancePackComplianceSummaryGroupKey, data)
