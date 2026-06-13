"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#GetProtectConfigurationCountryRuleSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn


class GetProtectConfigurationCountryRuleSetRequest(TypedDict):
    protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""
    number_capability: (
        "aws_sdk_pinpoint_sms_voice_v2.types.number_capability.NumberCapability"
    )
    """<p>The capability type to return the CountryRuleSet for. Valid values are <code>SMS</code>, <code>VOICE</code>, or <code>MMS</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProtectConfigurationCountryRuleSetRequest) -> dict:
    out: dict = {}
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["NumberCapability"] = value["number_capability"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetProtectConfigurationCountryRuleSetRequest:
    out: GetProtectConfigurationCountryRuleSetRequest = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "GetProtectConfigurationCountryRuleSetRequest.protect_configuration_id required"
        )
    if "NumberCapability" in data:
        out["number_capability"] = data["NumberCapability"]
    else:
        raise DeserializationError(
            "GetProtectConfigurationCountryRuleSetRequest.number_capability required"
        )
    return out
