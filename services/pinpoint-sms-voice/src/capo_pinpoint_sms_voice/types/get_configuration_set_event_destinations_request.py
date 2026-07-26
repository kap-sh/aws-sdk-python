"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#GetConfigurationSetEventDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.__string


class GetConfigurationSetEventDestinationsRequest(TypedDict, closed=True):
    configuration_set_name: "capo_pinpoint_sms_voice.types.__string.__string"
    """ConfigurationSetName"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationSetEventDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationSetEventDestinationsRequest:
    out: GetConfigurationSetEventDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out
