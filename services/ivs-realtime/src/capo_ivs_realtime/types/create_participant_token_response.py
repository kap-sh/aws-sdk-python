"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CreateParticipantTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_token


class CreateParticipantTokenResponse(TypedDict, closed=True):
    participant_token: NotRequired[
        "capo_ivs_realtime.types.participant_token.ParticipantToken"
    ]
    """<p>The participant token that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateParticipantTokenResponse) -> dict:
    out: dict = {}
    if "participant_token" in value:
        import capo_ivs_realtime.types.participant_token

        out["participantToken"] = (
            capo_ivs_realtime.types.participant_token.serialize_json(
                value["participant_token"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateParticipantTokenResponse:
    out: CreateParticipantTokenResponse = {}  # type: ignore[typeddict-item]
    if "participantToken" in data:
        import capo_ivs_realtime.types.participant_token

        out["participant_token"] = (
            capo_ivs_realtime.types.participant_token.deserialize_json(
                data["participantToken"]
            )
        )
    return out
