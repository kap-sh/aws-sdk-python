"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeleteConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.configuration_set_name
    import aws_sdk_pinpoint_email.types.event_destination_name


class DeleteConfigurationSetEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: (
        "aws_sdk_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that contains the event destination that you want to delete.</p>"""
    event_destination_name: (
        "aws_sdk_pinpoint_email.types.event_destination_name.EventDestinationName"
    )
    """<p>The name of the event destination that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationSetEventDestinationRequest:
    out: DeleteConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
