"""Generated from Smithy shape ``com.amazonaws.connect#CreateParticipantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.participant_id
    import capo_connect.types.participant_token_credentials


class CreateParticipantResponse(TypedDict, closed=True):
    participant_credentials: NotRequired[
        "capo_connect.types.participant_token_credentials.ParticipantTokenCredentials"
    ]
    """<p>The token used by the chat participant to call <code>CreateParticipantConnection</code>. The participant token is valid for the lifetime of a chat participant.</p>"""
    participant_id: NotRequired["capo_connect.types.participant_id.ParticipantId"]
    """<p>The identifier for a chat participant. The participantId for a chat participant is the same throughout the chat lifecycle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateParticipantResponse) -> dict:
    out: dict = {}
    if "participant_credentials" in value:
        import capo_connect.types.participant_token_credentials

        out["ParticipantCredentials"] = (
            capo_connect.types.participant_token_credentials.serialize_json(
                value["participant_credentials"]
            )
        )
    if "participant_id" in value:
        out["ParticipantId"] = value["participant_id"]
    return out


def deserialize_json(data: dict) -> CreateParticipantResponse:
    out: CreateParticipantResponse = {}  # type: ignore[typeddict-item]
    if "ParticipantCredentials" in data:
        import capo_connect.types.participant_token_credentials

        out["participant_credentials"] = (
            capo_connect.types.participant_token_credentials.deserialize_json(
                data["ParticipantCredentials"]
            )
        )
    if "ParticipantId" in data:
        out["participant_id"] = data["ParticipantId"]
    return out
