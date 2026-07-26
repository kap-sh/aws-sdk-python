"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleTriggerTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.organization_config_rule_trigger_type

OrganizationConfigRuleTriggerTypes: TypeAlias = list[
    "capo_config_service.types.organization_config_rule_trigger_type.OrganizationConfigRuleTriggerType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRuleTriggerTypes) -> list:
    import capo_config_service.types.organization_config_rule_trigger_type

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.organization_config_rule_trigger_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationConfigRuleTriggerTypes:
    import capo_config_service.types.organization_config_rule_trigger_type

    out: OrganizationConfigRuleTriggerTypes = []
    for item in data:
        out.append(
            capo_config_service.types.organization_config_rule_trigger_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
