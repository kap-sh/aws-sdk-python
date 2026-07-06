"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetConfigurationSetEventDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.configuration_set_name


class GetConfigurationSetEventDestinationsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "aws_sdk_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that contains the event destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationSetEventDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationSetEventDestinationsRequest:
    out: GetConfigurationSetEventDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out
