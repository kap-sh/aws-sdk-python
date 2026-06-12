"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#DeleteConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.__string


class DeleteConfigurationSetEventDestinationRequest(TypedDict):
    configuration_set_name: "aws_sdk_pinpoint_sms_voice.types.__string.__string"
    """ConfigurationSetName"""
    event_destination_name: "aws_sdk_pinpoint_sms_voice.types.__string.__string"
    """EventDestinationName"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationSetEventDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationSetEventDestinationRequest:
    out: DeleteConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
