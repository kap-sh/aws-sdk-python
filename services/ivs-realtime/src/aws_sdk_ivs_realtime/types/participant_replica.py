"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantReplica``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.replication_state
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.stage_session_id


class ParticipantReplica(TypedDict):
    source_stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage from which this participant is replicated.</p>"""
    participant_id: "aws_sdk_ivs_realtime.types.participant_id.ParticipantId"
    r"""<p>Participant ID of the publisher that will be replicated. This is assigned by IVS and returned by <a>CreateParticipantToken</a> or the <code>jti</code> (JWT ID) used to <a href=\"https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed\"> create a self signed token</a>.</p>"""
    source_session_id: "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of the session within the source stage.</p>"""
    destination_stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage where the participant is replicated.</p>"""
    destination_session_id: "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of the session within the destination stage.</p>"""
    replication_state: "aws_sdk_ivs_realtime.types.replication_state.ReplicationState"
    """<p>Replica’s current replication state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantReplica) -> dict:
    out: dict = {}
    out["sourceStageArn"] = value["source_stage_arn"]
    out["participantId"] = value["participant_id"]
    out["sourceSessionId"] = value["source_session_id"]
    out["destinationStageArn"] = value["destination_stage_arn"]
    out["destinationSessionId"] = value["destination_session_id"]
    out["replicationState"] = value["replication_state"]
    return out


def deserialize_json(data: dict) -> ParticipantReplica:
    out: ParticipantReplica = {}  # type: ignore[typeddict-item]
    if "sourceStageArn" in data:
        out["source_stage_arn"] = data["sourceStageArn"]
    else:
        raise DeserializationError("ParticipantReplica.source_stage_arn required")
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError("ParticipantReplica.participant_id required")
    if "sourceSessionId" in data:
        out["source_session_id"] = data["sourceSessionId"]
    else:
        raise DeserializationError("ParticipantReplica.source_session_id required")
    if "destinationStageArn" in data:
        out["destination_stage_arn"] = data["destinationStageArn"]
    else:
        raise DeserializationError("ParticipantReplica.destination_stage_arn required")
    if "destinationSessionId" in data:
        out["destination_session_id"] = data["destinationSessionId"]
    else:
        raise DeserializationError("ParticipantReplica.destination_session_id required")
    if "replicationState" in data:
        out["replication_state"] = data["replicationState"]
    else:
        raise DeserializationError("ParticipantReplica.replication_state required")
    return out
