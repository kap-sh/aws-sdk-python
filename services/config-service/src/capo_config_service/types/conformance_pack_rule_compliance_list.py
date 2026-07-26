"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackRuleComplianceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_rule_compliance

ConformancePackRuleComplianceList: TypeAlias = list[
    "capo_config_service.types.conformance_pack_rule_compliance.ConformancePackRuleCompliance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackRuleComplianceList) -> list:
    import capo_config_service.types.conformance_pack_rule_compliance

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.conformance_pack_rule_compliance.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackRuleComplianceList:
    import capo_config_service.types.conformance_pack_rule_compliance

    out: ConformancePackRuleComplianceList = []
    for item in data:
        out.append(
            capo_config_service.types.conformance_pack_rule_compliance.deserialize_aws_json_1_1(
                item
            )
        )
    return out
