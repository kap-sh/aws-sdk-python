"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateConformancePackComplianceSummaryGroupKey``."""

from typing import Literal, TypeAlias, cast

AggregateConformancePackComplianceSummaryGroupKey: TypeAlias = Literal[
    "ACCOUNT_ID",
    "AWS_REGION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AggregateConformancePackComplianceSummaryGroupKey,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> AggregateConformancePackComplianceSummaryGroupKey:
    return cast(AggregateConformancePackComplianceSummaryGroupKey, data)
