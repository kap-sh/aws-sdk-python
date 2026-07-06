"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteProtectConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn


class DeleteProtectConfigurationRequest(TypedDict, closed=True):
    protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    """<p>The unique identifier for the protect configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProtectConfigurationRequest) -> dict:
    out: dict = {}
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProtectConfigurationRequest:
    out: DeleteProtectConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "DeleteProtectConfigurationRequest.protect_configuration_id required"
        )
    return out
