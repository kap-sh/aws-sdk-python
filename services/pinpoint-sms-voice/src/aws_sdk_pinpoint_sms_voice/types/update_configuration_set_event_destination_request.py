"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#UpdateConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.__string
    import aws_sdk_pinpoint_sms_voice.types.event_destination_definition


class UpdateConfigurationSetEventDestinationRequest(TypedDict):
    configuration_set_name: "aws_sdk_pinpoint_sms_voice.types.__string.__string"
    """ConfigurationSetName"""
    event_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.event_destination_definition.EventDestinationDefinition"
    ]
    event_destination_name: "aws_sdk_pinpoint_sms_voice.types.__string.__string"
    """EventDestinationName"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    if "event_destination" in value:
        import aws_sdk_pinpoint_sms_voice.types.event_destination_definition

        out["EventDestination"] = (
            aws_sdk_pinpoint_sms_voice.types.event_destination_definition.serialize_json(
                value["event_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationSetEventDestinationRequest:
    out: UpdateConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if "EventDestination" in data:
        import aws_sdk_pinpoint_sms_voice.types.event_destination_definition

        out["event_destination"] = (
            aws_sdk_pinpoint_sms_voice.types.event_destination_definition.deserialize_json(
                data["EventDestination"]
            )
        )
    return out
