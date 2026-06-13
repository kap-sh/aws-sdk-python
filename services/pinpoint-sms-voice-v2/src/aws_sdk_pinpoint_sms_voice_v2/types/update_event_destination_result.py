"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateEventDestinationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name
    import aws_sdk_pinpoint_sms_voice_v2.types.event_destination


class UpdateEventDestinationResult(TypedDict):
    configuration_set_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the ConfigurationSet that was updated.</p>"""
    configuration_set_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set.</p>"""
    event_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.event_destination.EventDestination"
    ]
    """<p>An EventDestination object containing the details of where events will be logged. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEventDestinationResult) -> dict:
    out: dict = {}
    if "configuration_set_arn" in value:
        out["ConfigurationSetArn"] = value["configuration_set_arn"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "event_destination" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.event_destination

        out["EventDestination"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.event_destination.serialize_aws_json_1_0(
                value["event_destination"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEventDestinationResult:
    out: UpdateEventDestinationResult = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetArn" in data:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "EventDestination" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.event_destination

        out["event_destination"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.event_destination.deserialize_aws_json_1_0(
                data["EventDestination"]
            )
        )
    return out
