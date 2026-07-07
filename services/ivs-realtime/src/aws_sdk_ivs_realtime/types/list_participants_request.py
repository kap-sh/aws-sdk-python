"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListParticipantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.max_participant_results
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.participant_recording_filter_by_recording_state
    import aws_sdk_ivs_realtime.types.participant_state
    import aws_sdk_ivs_realtime.types.published
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.stage_session_id
    import aws_sdk_ivs_realtime.types.user_id


class ListParticipantsRequest(TypedDict, closed=True):
    stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>Stage ARN.</p>"""
    session_id: "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of the session within the stage.</p>"""
    filter_by_user_id: NotRequired["aws_sdk_ivs_realtime.types.user_id.UserId"]
    """<p>Filters the response list to match the specified user ID. Only one of <code>filterByUserId</code>, <code>filterByPublished</code>, <code>filterByState</code>, or <code>filterByRecordingState</code> can be provided per request. A <code>userId</code> is a customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems.</p>"""
    filter_by_published: "aws_sdk_ivs_realtime.types.published.Published"
    """<p>Filters the response list to only show participants who published during the stage session. Only one of <code>filterByUserId</code>, <code>filterByPublished</code>, <code>filterByState</code>, or <code>filterByRecordingState</code> can be provided per request.</p>"""
    filter_by_state: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_state.ParticipantState"
    ]
    """<p>Filters the response list to only show participants in the specified state. Only one of <code>filterByUserId</code>, <code>filterByPublished</code>, <code>filterByState</code>, or <code>filterByRecordingState</code> can be provided per request.</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>The first participant to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "aws_sdk_ivs_realtime.types.max_participant_results.MaxParticipantResults"
    ]
    """<p>Maximum number of results to return. Default: 50.</p>"""
    filter_by_recording_state: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_recording_filter_by_recording_state.ParticipantRecordingFilterByRecordingState"
    ]
    """<p>Filters the response list to only show participants with the specified recording state. Only one of <code>filterByUserId</code>, <code>filterByPublished</code>, <code>filterByState</code>, or <code>filterByRecordingState</code> can be provided per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListParticipantsRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    out["sessionId"] = value["session_id"]
    if "filter_by_user_id" in value:
        out["filterByUserId"] = value["filter_by_user_id"]
    out["filterByPublished"] = value.get("filter_by_published", False)
    if "filter_by_state" in value:
        out["filterByState"] = value["filter_by_state"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter_by_recording_state" in value:
        out["filterByRecordingState"] = value["filter_by_recording_state"]
    return out


def deserialize_json(data: dict) -> ListParticipantsRequest:
    out: ListParticipantsRequest = {}  # type: ignore[typeddict-item]
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("ListParticipantsRequest.stage_arn required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("ListParticipantsRequest.session_id required")
    if "filterByUserId" in data:
        out["filter_by_user_id"] = data["filterByUserId"]
    if "filterByPublished" in data:
        out["filter_by_published"] = data["filterByPublished"]
    else:
        out["filter_by_published"] = False
    if "filterByState" in data:
        out["filter_by_state"] = data["filterByState"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filterByRecordingState" in data:
        out["filter_by_recording_state"] = data["filterByRecordingState"]
    return out
