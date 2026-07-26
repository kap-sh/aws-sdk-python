"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AssociateProtectConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn


class AssociateProtectConfigurationRequest(TypedDict, closed=True):
    protect_configuration_id: "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""
    configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    """<p>The name of the ConfigurationSet.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateProtectConfigurationRequest) -> dict:
    out: dict = {}
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    out["ConfigurationSetName"] = value["configuration_set_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateProtectConfigurationRequest:
    out: AssociateProtectConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "AssociateProtectConfigurationRequest.protect_configuration_id required"
        )
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        raise DeserializationError(
            "AssociateProtectConfigurationRequest.configuration_set_name required"
        )
    return out
