"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.event_destination_definition
    import capo_sesv2.types.event_destination_name


class UpdateConfigurationSetEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that contains the event destination to modify.</p>"""
    event_destination_name: (
        "capo_sesv2.types.event_destination_name.EventDestinationName"
    )
    """<p>The name of the event destination.</p>"""
    event_destination: (
        "capo_sesv2.types.event_destination_definition.EventDestinationDefinition"
    )
    """<p>An object that defines the event destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.event_destination_definition

    out["EventDestination"] = (
        capo_sesv2.types.event_destination_definition.serialize_json(
            value["event_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationSetEventDestinationRequest:
    out: UpdateConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if "EventDestination" in data:
        import capo_sesv2.types.event_destination_definition

        out["event_destination"] = (
            capo_sesv2.types.event_destination_definition.deserialize_json(
                data["EventDestination"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfigurationSetEventDestinationRequest.event_destination required"
        )
    return out
