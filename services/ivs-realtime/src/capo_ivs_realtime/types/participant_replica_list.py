"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantReplicaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_replica

ParticipantReplicaList: TypeAlias = list[
    "capo_ivs_realtime.types.participant_replica.ParticipantReplica"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantReplicaList) -> list:
    import capo_ivs_realtime.types.participant_replica

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.participant_replica.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipantReplicaList:
    import capo_ivs_realtime.types.participant_replica

    out: ParticipantReplicaList = []
    for item in data:
        out.append(capo_ivs_realtime.types.participant_replica.deserialize_json(item))
    return out
