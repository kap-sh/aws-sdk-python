"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_summary

ParticipantList: TypeAlias = list[
    "capo_ivs_realtime.types.participant_summary.ParticipantSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantList) -> list:
    import capo_ivs_realtime.types.participant_summary

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.participant_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipantList:
    import capo_ivs_realtime.types.participant_summary

    out: ParticipantList = []
    for item in data:
        out.append(capo_ivs_realtime.types.participant_summary.deserialize_json(item))
    return out
