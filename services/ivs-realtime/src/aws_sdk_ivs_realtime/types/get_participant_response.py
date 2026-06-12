"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetParticipantResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant


class GetParticipantResponse(TypedDict):
    participant: NotRequired["aws_sdk_ivs_realtime.types.participant.Participant"]
    """<p>The participant that is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetParticipantResponse) -> dict:
    out: dict = {}
    if "participant" in value:
        import aws_sdk_ivs_realtime.types.participant

        out["participant"] = aws_sdk_ivs_realtime.types.participant.serialize_json(
            value["participant"]
        )
    return out


def deserialize_json(data: dict) -> GetParticipantResponse:
    out: GetParticipantResponse = {}  # type: ignore[typeddict-item]
    if "participant" in data:
        import aws_sdk_ivs_realtime.types.participant

        out["participant"] = aws_sdk_ivs_realtime.types.participant.deserialize_json(
            data["participant"]
        )
    return out
