"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name
    import aws_sdk_sesv2.types.event_destination_definition
    import aws_sdk_sesv2.types.event_destination_name


class CreateConfigurationSetEventDestinationRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set .</p>"""
    event_destination_name: (
        "aws_sdk_sesv2.types.event_destination_name.EventDestinationName"
    )
    """<p>A name that identifies the event destination within the configuration set.</p>"""
    event_destination: (
        "aws_sdk_sesv2.types.event_destination_definition.EventDestinationDefinition"
    )
    """<p>An object that defines the event destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    out["EventDestinationName"] = value["event_destination_name"]
    import aws_sdk_sesv2.types.event_destination_definition

    out["EventDestination"] = (
        aws_sdk_sesv2.types.event_destination_definition.serialize_json(
            value["event_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateConfigurationSetEventDestinationRequest:
    out: CreateConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if "EventDestinationName" in data:
        out["event_destination_name"] = data["EventDestinationName"]
    else:
        raise DeserializationError(
            "CreateConfigurationSetEventDestinationRequest.event_destination_name required"
        )
    if "EventDestination" in data:
        import aws_sdk_sesv2.types.event_destination_definition

        out["event_destination"] = (
            aws_sdk_sesv2.types.event_destination_definition.deserialize_json(
                data["EventDestination"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfigurationSetEventDestinationRequest.event_destination required"
        )
    return out
