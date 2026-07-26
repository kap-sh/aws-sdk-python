"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteDefaultSenderIdResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name
    import capo_pinpoint_sms_voice_v2.types.sender_id


class DeleteDefaultSenderIdResult(TypedDict, closed=True):
    configuration_set_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the configuration set.</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set.</p>"""
    sender_id: NotRequired["capo_pinpoint_sms_voice_v2.types.sender_id.SenderId"]
    """<p>The current sender ID for the configuration set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDefaultSenderIdResult) -> dict:
    out: dict = {}
    if "configuration_set_arn" in value:
        out["ConfigurationSetArn"] = value["configuration_set_arn"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "sender_id" in value:
        out["SenderId"] = value["sender_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDefaultSenderIdResult:
    out: DeleteDefaultSenderIdResult = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetArn" in data:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "SenderId" in data:
        out["sender_id"] = data["SenderId"]
    return out
