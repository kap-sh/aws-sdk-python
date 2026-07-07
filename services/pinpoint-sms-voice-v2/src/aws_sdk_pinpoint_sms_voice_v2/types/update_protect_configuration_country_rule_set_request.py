"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateProtectConfigurationCountryRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn


class UpdateProtectConfigurationCountryRuleSetRequest(TypedDict, closed=True):
    protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""
    number_capability: (
        "aws_sdk_pinpoint_sms_voice_v2.types.number_capability.NumberCapability"
    )
    """<p>The number capability to apply the CountryRuleSetUpdates updates to.</p>"""
    country_rule_set_updates: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.ProtectConfigurationCountryRuleSet"
    r"""<p>A map of ProtectConfigurationCountryRuleSetInformation objects that contain the details for the requested NumberCapability. The Key is the two-letter ISO country code. For a list of supported ISO country codes, see <a href=\"https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html\">Supported countries and regions (SMS channel)</a> in the End User Messaging SMS User Guide.</p> <p>For example, to set the United States as allowed and Canada as blocked, the <code>CountryRuleSetUpdates</code> would be formatted as: <code>\"CountryRuleSetUpdates\": { \"US\" : { \"ProtectStatus\": \"ALLOW\" } \"CA\" : { \"ProtectStatus\": \"BLOCK\" } }</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateProtectConfigurationCountryRuleSetRequest,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["NumberCapability"] = value["number_capability"]
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set

    out["CountryRuleSetUpdates"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.serialize_aws_json_1_0(
            value["country_rule_set_updates"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateProtectConfigurationCountryRuleSetRequest:
    out: UpdateProtectConfigurationCountryRuleSetRequest = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "UpdateProtectConfigurationCountryRuleSetRequest.protect_configuration_id required"
        )
    if "NumberCapability" in data:
        out["number_capability"] = data["NumberCapability"]
    else:
        raise DeserializationError(
            "UpdateProtectConfigurationCountryRuleSetRequest.number_capability required"
        )
    if "CountryRuleSetUpdates" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set

        out["country_rule_set_updates"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_country_rule_set.deserialize_aws_json_1_0(
                data["CountryRuleSetUpdates"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProtectConfigurationCountryRuleSetRequest.country_rule_set_updates required"
        )
    return out
