"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ProtectConfigurationCountryRuleSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set_information

ProtectConfigurationCountryRuleSet: TypeAlias = dict[
    "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode",
    "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set_information.ProtectConfigurationCountryRuleSetInformation",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    input_to_serialize: ProtectConfigurationCountryRuleSet,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set_information

        out[key] = (
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set_information.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProtectConfigurationCountryRuleSet:
    out: ProtectConfigurationCountryRuleSet = {}
    for key, value in data.items():
        import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set_information

        out[key] = (
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set_information.deserialize_aws_json_1_0(
                value
            )
        )
    return out
