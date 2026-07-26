"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ProtectConfigurationRuleSetNumberOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override

ProtectConfigurationRuleSetNumberOverrideList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override.ProtectConfigurationRuleSetNumberOverride"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ProtectConfigurationRuleSetNumberOverrideList,
) -> list:
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ProtectConfigurationRuleSetNumberOverrideList:
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override

    out: ProtectConfigurationRuleSetNumberOverrideList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override.deserialize_aws_json_1_0(
                item
            )
        )
    return out
