"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorExternalSystemsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class GetVoiceConnectorExternalSystemsConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The ID of the Voice Connector for which to return information about the external system configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorExternalSystemsConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> GetVoiceConnectorExternalSystemsConfigurationRequest:
    out: GetVoiceConnectorExternalSystemsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
