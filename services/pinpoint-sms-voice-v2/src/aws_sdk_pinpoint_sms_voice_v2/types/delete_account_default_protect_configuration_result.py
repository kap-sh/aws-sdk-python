"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteAccountDefaultProtectConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id


class DeleteAccountDefaultProtectConfigurationResult(TypedDict):
    default_protect_configuration_arn: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the account default protect configuration.</p>"""
    default_protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier of the account default protect configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DeleteAccountDefaultProtectConfigurationResult,
) -> dict:
    out: dict = {}
    out["DefaultProtectConfigurationArn"] = value["default_protect_configuration_arn"]
    out["DefaultProtectConfigurationId"] = value["default_protect_configuration_id"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DeleteAccountDefaultProtectConfigurationResult:
    out: DeleteAccountDefaultProtectConfigurationResult = {}  # type: ignore[typeddict-item]
    if "DefaultProtectConfigurationArn" in data:
        out["default_protect_configuration_arn"] = data[
            "DefaultProtectConfigurationArn"
        ]
    else:
        raise DeserializationError(
            "DeleteAccountDefaultProtectConfigurationResult.default_protect_configuration_arn required"
        )
    if "DefaultProtectConfigurationId" in data:
        out["default_protect_configuration_id"] = data["DefaultProtectConfigurationId"]
    else:
        raise DeserializationError(
            "DeleteAccountDefaultProtectConfigurationResult.default_protect_configuration_id required"
        )
    return out
