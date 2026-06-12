"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name
    import aws_sdk_sesv2.types.event_destination_name


class DeleteConfigurationSetEventDestinationRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that contains the event destination to delete.</p>"""
    event_destination_name: (
        "aws_sdk_sesv2.types.event_destination_name.EventDestinationName"
    )
    """<p>The name of the event destination to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationSetEventDestinationRequest:
    out: DeleteConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
