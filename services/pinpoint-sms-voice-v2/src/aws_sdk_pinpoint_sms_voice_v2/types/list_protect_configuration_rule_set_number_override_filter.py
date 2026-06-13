"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListProtectConfigurationRuleSetNumberOverrideFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_filter_item

ListProtectConfigurationRuleSetNumberOverrideFilter: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_filter_item.ProtectConfigurationRuleSetNumberOverrideFilterItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListProtectConfigurationRuleSetNumberOverrideFilter,
) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_filter_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_filter_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ListProtectConfigurationRuleSetNumberOverrideFilter:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_filter_item

    out: ListProtectConfigurationRuleSetNumberOverrideFilter = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_filter_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
