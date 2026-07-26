"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorTerminationCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.credential_list
    import capo_chime_sdk_voice.types.non_empty_string


class PutVoiceConnectorTerminationCredentialsRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""
    credentials: NotRequired[
        "capo_chime_sdk_voice.types.credential_list.CredentialList"
    ]
    """<p>The termination credentials being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorTerminationCredentialsRequest) -> dict:
    out: dict = {}
    if "credentials" in value:
        import capo_chime_sdk_voice.types.credential_list

        out["Credentials"] = capo_chime_sdk_voice.types.credential_list.serialize_json(
            value["credentials"]
        )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorTerminationCredentialsRequest:
    out: PutVoiceConnectorTerminationCredentialsRequest = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import capo_chime_sdk_voice.types.credential_list

        out["credentials"] = (
            capo_chime_sdk_voice.types.credential_list.deserialize_json(
                data["Credentials"]
            )
        )
    return out
