"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#CreateConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.__string
    import capo_pinpoint_sms_voice.types.event_destination_definition
    import capo_pinpoint_sms_voice.types.non_empty_string


class CreateConfigurationSetEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: "capo_pinpoint_sms_voice.types.__string.__string"
    """ConfigurationSetName"""
    event_destination: NotRequired[
        "capo_pinpoint_sms_voice.types.event_destination_definition.EventDestinationDefinition"
    ]
    event_destination_name: NotRequired[
        "capo_pinpoint_sms_voice.types.non_empty_string.NonEmptyString"
    ]
    """A name that identifies the event destination."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    if "event_destination" in value:
        import capo_pinpoint_sms_voice.types.event_destination_definition

        out["EventDestination"] = (
            capo_pinpoint_sms_voice.types.event_destination_definition.serialize_json(
                value["event_destination"]
            )
        )
    if "event_destination_name" in value:
        out["EventDestinationName"] = value["event_destination_name"]
    return out


def deserialize_json(data: dict) -> CreateConfigurationSetEventDestinationRequest:
    out: CreateConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if "EventDestination" in data:
        import capo_pinpoint_sms_voice.types.event_destination_definition

        out["event_destination"] = (
            capo_pinpoint_sms_voice.types.event_destination_definition.deserialize_json(
                data["EventDestination"]
            )
        )
    if "EventDestinationName" in data:
        out["event_destination_name"] = data["EventDestinationName"]
    return out
