"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorOriginationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.origination


class PutVoiceConnectorOriginationRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""
    origination: "capo_chime_sdk_voice.types.origination.Origination"
    """<p>The origination settings being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorOriginationRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.origination

    out["Origination"] = capo_chime_sdk_voice.types.origination.serialize_json(
        value["origination"]
    )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorOriginationRequest:
    out: PutVoiceConnectorOriginationRequest = {}  # type: ignore[typeddict-item]
    if "Origination" in data:
        import capo_chime_sdk_voice.types.origination

        out["origination"] = capo_chime_sdk_voice.types.origination.deserialize_json(
            data["Origination"]
        )
    else:
        raise DeserializationError(
            "PutVoiceConnectorOriginationRequest.origination required"
        )
    return out
