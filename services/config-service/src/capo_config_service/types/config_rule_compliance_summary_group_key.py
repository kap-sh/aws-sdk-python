"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRuleComplianceSummaryGroupKey``."""

from typing import Literal, TypeAlias, cast

ConfigRuleComplianceSummaryGroupKey: TypeAlias = Literal[
    "ACCOUNT_ID",
    "AWS_REGION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRuleComplianceSummaryGroupKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigRuleComplianceSummaryGroupKey:
    return cast(ConfigRuleComplianceSummaryGroupKey, data)
