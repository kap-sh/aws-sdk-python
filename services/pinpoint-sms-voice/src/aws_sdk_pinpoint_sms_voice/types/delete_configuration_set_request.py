"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#DeleteConfigurationSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.__string


class DeleteConfigurationSetRequest(TypedDict):
    configuration_set_name: "aws_sdk_pinpoint_sms_voice.types.__string.__string"
    """ConfigurationSetName"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationSetRequest:
    out: DeleteConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    return out
