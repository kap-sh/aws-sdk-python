"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#GetProtectConfigurationCountryRuleSetResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id


class GetProtectConfigurationCountryRuleSetResult(TypedDict):
    protect_configuration_arn: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""
    number_capability: (
        "aws_sdk_pinpoint_sms_voice_v2.types.number_capability.NumberCapability"
    )
    """<p>The capability type associated with the returned ProtectConfigurationCountryRuleSetInformation objects.</p>"""
    country_rule_set: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.ProtectConfigurationCountryRuleSet"
    """<p>A map of ProtectConfigurationCountryRuleSetInformation objects that contain the details for the requested NumberCapability. The Key is the two-letter ISO country code. For a list of supported ISO country codes, see <a href=\"https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html\">Supported countries and regions (SMS channel)</a> in the End User Messaging SMS User Guide.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProtectConfigurationCountryRuleSetResult) -> dict:
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


def deserialize_aws_json_1_0(data: dict) -> GetProtectConfigurationCountryRuleSetResult:
    out: GetProtectConfigurationCountryRuleSetResult = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationArn" in data:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        raise DeserializationError(
            "GetProtectConfigurationCountryRuleSetResult.protect_configuration_arn required"
        )
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "GetProtectConfigurationCountryRuleSetResult.protect_configuration_id required"
        )
    if "NumberCapability" in data:
        out["number_capability"] = data["NumberCapability"]
    else:
        raise DeserializationError(
            "GetProtectConfigurationCountryRuleSetResult.number_capability required"
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
            "GetProtectConfigurationCountryRuleSetResult.country_rule_set required"
        )
    return out
