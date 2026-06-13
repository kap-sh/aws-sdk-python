"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateProtectConfigurationCountryRuleSetResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id


class UpdateProtectConfigurationCountryRuleSetResult(TypedDict):
    protect_configuration_arn: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""
    number_capability: (
        "aws_sdk_pinpoint_sms_voice_v2.types.number_capability.NumberCapability"
    )
    """<p>The number capability that was updated</p>"""
    country_rule_set: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.ProtectConfigurationCountryRuleSet"
    """<p>An array of ProtectConfigurationCountryRuleSetInformation containing the rules for the NumberCapability.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateProtectConfigurationCountryRuleSetResult,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationArn"] = value["protect_configuration_arn"]
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["NumberCapability"] = value["number_capability"]
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set

    out["CountryRuleSet"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.serialize_aws_json_1_0(
            value["country_rule_set"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateProtectConfigurationCountryRuleSetResult:
    out: UpdateProtectConfigurationCountryRuleSetResult = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationArn" in data:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateProtectConfigurationCountryRuleSetResult.protect_configuration_arn required"
        )
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "UpdateProtectConfigurationCountryRuleSetResult.protect_configuration_id required"
        )
    if "NumberCapability" in data:
        out["number_capability"] = data["NumberCapability"]
    else:
        raise DeserializationError(
            "UpdateProtectConfigurationCountryRuleSetResult.number_capability required"
        )
    if "CountryRuleSet" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set

        out["country_rule_set"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.deserialize_aws_json_1_0(
                data["CountryRuleSet"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProtectConfigurationCountryRuleSetResult.country_rule_set required"
        )
    return out
