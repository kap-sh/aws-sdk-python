"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StopParticipantReplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.stage_arn


class StopParticipantReplicationRequest(TypedDict):
    source_stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage where the participant is publishing.</p>"""
    destination_stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage where the participant has been replicated.</p>"""
    participant_id: "aws_sdk_ivs_realtime.types.participant_id.ParticipantId"
    r"""<p>Participant ID of the publisher that has been replicated. This is assigned by IVS and returned by <a>CreateParticipantToken</a> or the <code>jti</code> (JWT ID) used to <a href=\"https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed\"> create a self signed token</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopParticipantReplicationRequest) -> dict:
    out: dict = {}
    out["sourceStageArn"] = value["source_stage_arn"]
    out["destinationStageArn"] = value["destination_stage_arn"]
    out["participantId"] = value["participant_id"]
    return out


def deserialize_json(data: dict) -> StopParticipantReplicationRequest:
    out: StopParticipantReplicationRequest = {}  # type: ignore[typeddict-item]
    if "sourceStageArn" in data:
        out["source_stage_arn"] = data["sourceStageArn"]
    else:
        raise DeserializationError(
            "StopParticipantReplicationRequest.source_stage_arn required"
        )
    if "destinationStageArn" in data:
        out["destination_stage_arn"] = data["destinationStageArn"]
    else:
        raise DeserializationError(
            "StopParticipantReplicationRequest.destination_stage_arn required"
        )
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError(
            "StopParticipantReplicationRequest.participant_id required"
        )
    return out
