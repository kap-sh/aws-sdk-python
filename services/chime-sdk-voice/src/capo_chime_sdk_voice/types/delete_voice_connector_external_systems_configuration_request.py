"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceConnectorExternalSystemsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string


class DeleteVoiceConnectorExternalSystemsConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
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
