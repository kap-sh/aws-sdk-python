"""Generated from Smithy shape ``com.amazonaws.pinpointemail#UpdateConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.configuration_set_name
    import aws_sdk_pinpoint_email.types.event_destination_definition
    import aws_sdk_pinpoint_email.types.event_destination_name


class UpdateConfigurationSetEventDestinationRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that contains the event destination that you want to modify.</p>"""
    event_destination_name: (
        "aws_sdk_pinpoint_email.types.event_destination_name.EventDestinationName"
    )
    """<p>The name of the event destination that you want to modify.</p>"""
    event_destination: "aws_sdk_pinpoint_email.types.event_destination_definition.EventDestinationDefinition"
    """<p>An object that defines the event destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_email.types.event_destination_definition

    out["EventDestination"] = (
        aws_sdk_pinpoint_email.types.event_destination_definition.serialize_json(
            value["event_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationSetEventDestinationRequest:
    out: UpdateConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if "EventDestination" in data:
        import aws_sdk_pinpoint_email.types.event_destination_definition

        out["event_destination"] = (
            aws_sdk_pinpoint_email.types.event_destination_definition.deserialize_json(
                data["EventDestination"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfigurationSetEventDestinationRequest.event_destination required"
        )
    return out
