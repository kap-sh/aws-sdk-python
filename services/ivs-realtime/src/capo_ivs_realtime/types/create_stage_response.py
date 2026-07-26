"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CreateStageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_token_list
    import capo_ivs_realtime.types.stage


class CreateStageResponse(TypedDict, closed=True):
    stage: NotRequired["capo_ivs_realtime.types.stage.Stage"]
    """<p>The stage that was created.</p>"""
    participant_tokens: NotRequired[
        "capo_ivs_realtime.types.participant_token_list.ParticipantTokenList"
    ]
    """<p>Participant tokens attached to the stage. These correspond to the <code>participants</code> in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStageResponse) -> dict:
    out: dict = {}
    if "stage" in value:
        import capo_ivs_realtime.types.stage

        out["stage"] = capo_ivs_realtime.types.stage.serialize_json(value["stage"])
    if "participant_tokens" in value:
        import capo_ivs_realtime.types.participant_token_list

        out["participantTokens"] = (
            capo_ivs_realtime.types.participant_token_list.serialize_json(
                value["participant_tokens"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateStageResponse:
    out: CreateStageResponse = {}  # type: ignore[typeddict-item]
    if "stage" in data:
        import capo_ivs_realtime.types.stage

        out["stage"] = capo_ivs_realtime.types.stage.deserialize_json(data["stage"])
    if "participantTokens" in data:
        import capo_ivs_realtime.types.participant_token_list

        out["participant_tokens"] = (
            capo_ivs_realtime.types.participant_token_list.deserialize_json(
                data["participantTokens"]
            )
        )
    return out
