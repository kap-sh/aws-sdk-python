"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteProtectConfigurationRuleSetNumberOverrideRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn


class DeleteProtectConfigurationRuleSetNumberOverrideRequest(TypedDict):
    protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""
    destination_phone_number: (
        "aws_sdk_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DeleteProtectConfigurationRuleSetNumberOverrideRequest,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DeleteProtectConfigurationRuleSetNumberOverrideRequest:
    out: DeleteProtectConfigurationRuleSetNumberOverrideRequest = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "DeleteProtectConfigurationRuleSetNumberOverrideRequest.protect_configuration_id required"
        )
    if "DestinationPhoneNumber" in data:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "DeleteProtectConfigurationRuleSetNumberOverrideRequest.destination_phone_number required"
        )
    return out
