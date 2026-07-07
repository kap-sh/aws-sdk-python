"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteDefaultMessageTypeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name
    import aws_sdk_pinpoint_sms_voice_v2.types.message_type


class DeleteDefaultMessageTypeResult(TypedDict, closed=True):
    configuration_set_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the configuration set.</p>"""
    configuration_set_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set.</p>"""
    message_type: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.message_type.MessageType"
    ]
    """<p>The current message type for the configuration set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDefaultMessageTypeResult) -> dict:
    out: dict = {}
    if "configuration_set_arn" in value:
        out["ConfigurationSetArn"] = value["configuration_set_arn"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "message_type" in value:
        out["MessageType"] = value["message_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDefaultMessageTypeResult:
    out: DeleteDefaultMessageTypeResult = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetArn" in data:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "MessageType" in data:
        out["message_type"] = data["MessageType"]
    return out
