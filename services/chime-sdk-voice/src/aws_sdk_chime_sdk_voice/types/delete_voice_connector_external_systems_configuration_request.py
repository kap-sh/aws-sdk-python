"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceConnectorExternalSystemsConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class DeleteVoiceConnectorExternalSystemsConfigurationRequest(TypedDict):
    voice_connector_id: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The ID of the Voice Connector for which to delete the external system configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DeleteVoiceConnectorExternalSystemsConfigurationRequest,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> DeleteVoiceConnectorExternalSystemsConfigurationRequest:
    out: DeleteVoiceConnectorExternalSystemsConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
