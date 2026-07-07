"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListStageSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.stage_session_list


class ListStageSessionsResponse(TypedDict, closed=True):
    stage_sessions: "aws_sdk_ivs_realtime.types.stage_session_list.StageSessionList"
    """<p>List of matching stage sessions.</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>If there are more stage sessions than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStageSessionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs_realtime.types.stage_session_list

    out["stageSessions"] = aws_sdk_ivs_realtime.types.stage_session_list.serialize_json(
        value["stage_sessions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStageSessionsResponse:
    out: ListStageSessionsResponse = {}  # type: ignore[typeddict-item]
    if "stageSessions" in data:
        import aws_sdk_ivs_realtime.types.stage_session_list

        out["stage_sessions"] = (
            aws_sdk_ivs_realtime.types.stage_session_list.deserialize_json(
                data["stageSessions"]
            )
        )
    else:
        raise DeserializationError("ListStageSessionsResponse.stage_sessions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
