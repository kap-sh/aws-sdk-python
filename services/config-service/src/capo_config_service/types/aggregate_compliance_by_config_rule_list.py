"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateComplianceByConfigRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.aggregate_compliance_by_config_rule

AggregateComplianceByConfigRuleList: TypeAlias = list[
    "capo_config_service.types.aggregate_compliance_by_config_rule.AggregateComplianceByConfigRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateComplianceByConfigRuleList) -> list:
    import capo_config_service.types.aggregate_compliance_by_config_rule

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.aggregate_compliance_by_config_rule.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregateComplianceByConfigRuleList:
    import capo_config_service.types.aggregate_compliance_by_config_rule

    out: AggregateComplianceByConfigRuleList = []
    for item in data:
        out.append(
            capo_config_service.types.aggregate_compliance_by_config_rule.deserialize_aws_json_1_1(
                item
            )
        )
    return out
