"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetParticipantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.stage_session_id


class GetParticipantRequest(TypedDict):
    stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>Stage ARN.</p>"""
    session_id: "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of a session within the stage.</p>"""
    participant_id: "aws_sdk_ivs_realtime.types.participant_id.ParticipantId"
    """<p>Unique identifier for the participant. This is assigned by IVS and returned by <a>CreateParticipantToken</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetParticipantRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    out["sessionId"] = value["session_id"]
    out["participantId"] = value["participant_id"]
    return out


def deserialize_json(data: dict) -> GetParticipantRequest:
    out: GetParticipantRequest = {}  # type: ignore[typeddict-item]
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("GetParticipantRequest.stage_arn required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("GetParticipantRequest.session_id required")
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError("GetParticipantRequest.participant_id required")
    return out
