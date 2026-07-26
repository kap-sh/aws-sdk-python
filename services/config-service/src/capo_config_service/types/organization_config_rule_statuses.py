"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.organization_config_rule_status

OrganizationConfigRuleStatuses: TypeAlias = list[
    "capo_config_service.types.organization_config_rule_status.OrganizationConfigRuleStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRuleStatuses) -> list:
    import capo_config_service.types.organization_config_rule_status

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.organization_config_rule_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationConfigRuleStatuses:
    import capo_config_service.types.organization_config_rule_status

    out: OrganizationConfigRuleStatuses = []
    for item in data:
        out.append(
            capo_config_service.types.organization_config_rule_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
