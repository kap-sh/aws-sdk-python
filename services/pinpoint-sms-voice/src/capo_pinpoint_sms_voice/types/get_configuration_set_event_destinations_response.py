"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#GetConfigurationSetEventDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.event_destinations


class GetConfigurationSetEventDestinationsResponse(TypedDict, closed=True):
    event_destinations: NotRequired[
        "capo_pinpoint_sms_voice.types.event_destinations.EventDestinations"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationSetEventDestinationsResponse) -> dict:
    out: dict = {}
    if "event_destinations" in value:
        import capo_pinpoint_sms_voice.types.event_destinations

        out["EventDestinations"] = (
            capo_pinpoint_sms_voice.types.event_destinations.serialize_json(
                value["event_destinations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationSetEventDestinationsResponse:
    out: GetConfigurationSetEventDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "EventDestinations" in data:
        import capo_pinpoint_sms_voice.types.event_destinations

        out["event_destinations"] = (
            capo_pinpoint_sms_voice.types.event_destinations.deserialize_json(
                data["EventDestinations"]
            )
        )
    return out
