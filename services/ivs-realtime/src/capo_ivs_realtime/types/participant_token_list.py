"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_token

ParticipantTokenList: TypeAlias = list[
    "capo_ivs_realtime.types.participant_token.ParticipantToken"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenList) -> list:
    import capo_ivs_realtime.types.participant_token

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.participant_token.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipantTokenList:
    import capo_ivs_realtime.types.participant_token

    out: ParticipantTokenList = []
    for item in data:
        out.append(capo_ivs_realtime.types.participant_token.deserialize_json(item))
    return out
