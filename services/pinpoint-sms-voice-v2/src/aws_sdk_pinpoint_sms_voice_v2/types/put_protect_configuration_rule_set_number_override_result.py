"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutProtectConfigurationRuleSetNumberOverrideResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_override_action


class PutProtectConfigurationRuleSetNumberOverrideResult(TypedDict):
    protect_configuration_arn: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""
    destination_phone_number: (
        "aws_sdk_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the rule was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""
    action: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_override_action.ProtectConfigurationRuleOverrideAction"
    """<p>The action for the rule to take.</p>"""
    iso_country_code: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.</p>"""
    expiration_timestamp: NotRequired["datetime.datetime"]
    """<p>The time the rule will expire at.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: PutProtectConfigurationRuleSetNumberOverrideResult,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationArn"] = value["protect_configuration_arn"]
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    out["Action"] = value["action"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    if "expiration_timestamp" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["ExpirationTimestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expiration_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> PutProtectConfigurationRuleSetNumberOverrideResult:
    out: PutProtectConfigurationRuleSetNumberOverrideResult = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationArn" in data:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        raise DeserializationError(
            "PutProtectConfigurationRuleSetNumberOverrideResult.protect_configuration_arn required"
        )
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "PutProtectConfigurationRuleSetNumberOverrideResult.protect_configuration_id required"
        )
    if "DestinationPhoneNumber" in data:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "PutProtectConfigurationRuleSetNumberOverrideResult.destination_phone_number required"
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "PutProtectConfigurationRuleSetNumberOverrideResult.created_timestamp required"
        )
    if "Action" in data:
        out["action"] = data["Action"]
    else:
        raise DeserializationError(
            "PutProtectConfigurationRuleSetNumberOverrideResult.action required"
        )
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    if "ExpirationTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["expiration_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ExpirationTimestamp"]
            )
        )
    return out
