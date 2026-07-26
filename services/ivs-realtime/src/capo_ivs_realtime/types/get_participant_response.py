"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetParticipantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant


class GetParticipantResponse(TypedDict, closed=True):
    participant: NotRequired["capo_ivs_realtime.types.participant.Participant"]
    """<p>The participant that is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetParticipantResponse) -> dict:
    out: dict = {}
    if "participant" in value:
        import capo_ivs_realtime.types.participant

        out["participant"] = capo_ivs_realtime.types.participant.serialize_json(
            value["participant"]
        )
    return out


def deserialize_json(data: dict) -> GetParticipantResponse:
    out: GetParticipantResponse = {}  # type: ignore[typeddict-item]
    if "participant" in data:
        import capo_ivs_realtime.types.participant

        out["participant"] = capo_ivs_realtime.types.participant.deserialize_json(
            data["participant"]
        )
    return out
