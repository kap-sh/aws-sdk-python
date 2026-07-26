"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteEventDestinationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name
    import capo_pinpoint_sms_voice_v2.types.event_destination


class DeleteEventDestinationResult(TypedDict, closed=True):
    configuration_set_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the configuration set.</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set the event destination was deleted from.</p>"""
    event_destination: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.event_destination.EventDestination"
    ]
    """<p>The event destination object that was deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEventDestinationResult) -> dict:
    out: dict = {}
    if "configuration_set_arn" in value:
        out["ConfigurationSetArn"] = value["configuration_set_arn"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "event_destination" in value:
        import capo_pinpoint_sms_voice_v2.types.event_destination

        out["EventDestination"] = (
            capo_pinpoint_sms_voice_v2.types.event_destination.serialize_aws_json_1_0(
                value["event_destination"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEventDestinationResult:
    out: DeleteEventDestinationResult = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetArn" in data:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "EventDestination" in data:
        import capo_pinpoint_sms_voice_v2.types.event_destination

        out["event_destination"] = (
            capo_pinpoint_sms_voice_v2.types.event_destination.deserialize_aws_json_1_0(
                data["EventDestination"]
            )
        )
    return out
