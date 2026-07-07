"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListParticipantEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.max_participant_event_results
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.stage_session_id


class ListParticipantEventsRequest(TypedDict, closed=True):
    stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>Stage ARN.</p>"""
    session_id: "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of a session within the stage.</p>"""
    participant_id: "aws_sdk_ivs_realtime.types.participant_id.ParticipantId"
    """<p>Unique identifier for this participant. This is assigned by IVS and returned by <a>CreateParticipantToken</a>.</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>The first participant event to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "aws_sdk_ivs_realtime.types.max_participant_event_results.MaxParticipantEventResults"
    ]
    """<p>Maximum number of results to return. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListParticipantEventsRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    out["sessionId"] = value["session_id"]
    out["participantId"] = value["participant_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListParticipantEventsRequest:
    out: ListParticipantEventsRequest = {}  # type: ignore[typeddict-item]
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("ListParticipantEventsRequest.stage_arn required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("ListParticipantEventsRequest.session_id required")
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError(
            "ListParticipantEventsRequest.participant_id required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
