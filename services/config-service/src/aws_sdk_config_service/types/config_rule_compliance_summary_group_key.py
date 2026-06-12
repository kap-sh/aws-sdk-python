"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRuleComplianceSummaryGroupKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ConfigRuleComplianceSummaryGroupKey: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ConfigRuleComplianceSummaryGroupKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigRuleComplianceSummaryGroupKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigRuleComplianceSummaryGroupKey value: {data!r}"
        )
    return cast(ConfigRuleComplianceSummaryGroupKey, data)
