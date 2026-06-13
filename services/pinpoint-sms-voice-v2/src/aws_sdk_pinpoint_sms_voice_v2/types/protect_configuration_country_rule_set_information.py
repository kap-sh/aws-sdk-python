"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ProtectConfigurationCountryRuleSetInformation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_status


class ProtectConfigurationCountryRuleSetInformation(TypedDict):
    protect_status: "aws_sdk_pinpoint_sms_voice_v2.types.protect_status.ProtectStatus"
    """<p>The types of protection that can be used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ProtectConfigurationCountryRuleSetInformation,
) -> dict:
    out: dict = {}
    out["ProtectStatus"] = value["protect_status"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ProtectConfigurationCountryRuleSetInformation:
    out: ProtectConfigurationCountryRuleSetInformation = {}  # type: ignore[typeddict-item]
    if "ProtectStatus" in data:
        out["protect_status"] = data["ProtectStatus"]
    else:
        raise DeserializationError(
            "ProtectConfigurationCountryRuleSetInformation.protect_status required"
        )
    return out
