"""Generated from Smithy shape ``com.amazonaws.sesv2#GetConfigurationSetEventDestinationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.event_destinations


class GetConfigurationSetEventDestinationsResponse(TypedDict):
    event_destinations: NotRequired[
        "aws_sdk_sesv2.types.event_destinations.EventDestinations"
    ]
    """<p>An array that includes all of the events destinations that have been configured for the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationSetEventDestinationsResponse) -> dict:
    out: dict = {}
    if "event_destinations" in value:
        import aws_sdk_sesv2.types.event_destinations

        out["EventDestinations"] = (
            aws_sdk_sesv2.types.event_destinations.serialize_json(
                value["event_destinations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationSetEventDestinationsResponse:
    out: GetConfigurationSetEventDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "EventDestinations" in data:
        import aws_sdk_sesv2.types.event_destinations

        out["event_destinations"] = (
            aws_sdk_sesv2.types.event_destinations.deserialize_json(
                data["EventDestinations"]
            )
        )
    return out
