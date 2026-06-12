"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetStageSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.stage_session_id


class GetStageSessionRequest(TypedDict):
    stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage for which the information is to be retrieved.</p>"""
    session_id: "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of a session within the stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageSessionRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> GetStageSessionRequest:
    out: GetStageSessionRequest = {}  # type: ignore[typeddict-item]
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("GetStageSessionRequest.stage_arn required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("GetStageSessionRequest.session_id required")
    return out
