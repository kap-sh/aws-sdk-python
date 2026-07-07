"""Generated from Smithy shape ``com.amazonaws.ivs#ListStreamSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.pagination_token
    import aws_sdk_ivs.types.stream_session_list


class ListStreamSessionsResponse(TypedDict, closed=True):
    stream_sessions: "aws_sdk_ivs.types.stream_session_list.StreamSessionList"
    """<p>List of stream sessions.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more streams than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamSessionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.stream_session_list

    out["streamSessions"] = aws_sdk_ivs.types.stream_session_list.serialize_json(
        value["stream_sessions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamSessionsResponse:
    out: ListStreamSessionsResponse = {}  # type: ignore[typeddict-item]
    if "streamSessions" in data:
        import aws_sdk_ivs.types.stream_session_list

        out["stream_sessions"] = aws_sdk_ivs.types.stream_session_list.deserialize_json(
            data["streamSessions"]
        )
    else:
        raise DeserializationError(
            "ListStreamSessionsResponse.stream_sessions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
