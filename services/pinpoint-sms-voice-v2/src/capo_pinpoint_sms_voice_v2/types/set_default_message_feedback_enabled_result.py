"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetDefaultMessageFeedbackEnabledResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name


class SetDefaultMessageFeedbackEnabledResult(TypedDict, closed=True):
    configuration_set_arn: NotRequired["str"]
    """<p>The arn of the configuration set.</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration.</p>"""
    message_feedback_enabled: NotRequired["bool"]
    """<p>True if message feedback is enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetDefaultMessageFeedbackEnabledResult) -> dict:
    out: dict = {}
    if "configuration_set_arn" in value:
        out["ConfigurationSetArn"] = value["configuration_set_arn"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "message_feedback_enabled" in value:
        out["MessageFeedbackEnabled"] = value["message_feedback_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetDefaultMessageFeedbackEnabledResult:
    out: SetDefaultMessageFeedbackEnabledResult = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetArn" in data:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "MessageFeedbackEnabled" in data:
        out["message_feedback_enabled"] = data["MessageFeedbackEnabled"]
    return out
