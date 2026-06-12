"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#GetConfigurationSetEventDestinationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.__string


class GetConfigurationSetEventDestinationsRequest(TypedDict):
    configuration_set_name: "aws_sdk_pinpoint_sms_voice.types.__string.__string"
    """ConfigurationSetName"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationSetEventDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationSetEventDestinationsRequest:
    out: GetConfigurationSetEventDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out
