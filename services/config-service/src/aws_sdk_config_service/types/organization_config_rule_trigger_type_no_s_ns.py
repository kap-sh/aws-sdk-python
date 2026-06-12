"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleTriggerTypeNoSNs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_config_rule_trigger_type_no_sn

OrganizationConfigRuleTriggerTypeNoSNs: TypeAlias = list[
    "aws_sdk_config_service.types.organization_config_rule_trigger_type_no_sn.OrganizationConfigRuleTriggerTypeNoSN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRuleTriggerTypeNoSNs) -> list:
    import aws_sdk_config_service.types.organization_config_rule_trigger_type_no_sn

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.organization_config_rule_trigger_type_no_sn.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationConfigRuleTriggerTypeNoSNs:
    import aws_sdk_config_service.types.organization_config_rule_trigger_type_no_sn

    out: OrganizationConfigRuleTriggerTypeNoSNs = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.organization_config_rule_trigger_type_no_sn.deserialize_aws_json_1_1(
                item
            )
        )
    return out
