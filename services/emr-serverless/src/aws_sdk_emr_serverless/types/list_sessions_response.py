"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.next_token
    import aws_sdk_emr_serverless.types.sessions


class ListSessionsResponse(TypedDict, closed=True):
    sessions: "aws_sdk_emr_serverless.types.sessions.Sessions"
    """<p>The output lists information about the specified sessions.</p>"""
    next_token: NotRequired["aws_sdk_emr_serverless.types.next_token.NextToken"]
    """<p>The output displays the token for the next set of session results. This is required for pagination and is available as a response of the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_emr_serverless.types.sessions

    out["sessions"] = aws_sdk_emr_serverless.types.sessions.serialize_json(
        value["sessions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionsResponse:
    out: ListSessionsResponse = {}  # type: ignore[typeddict-item]
    if "sessions" in data:
        import aws_sdk_emr_serverless.types.sessions

        out["sessions"] = aws_sdk_emr_serverless.types.sessions.deserialize_json(
            data["sessions"]
        )
    else:
        raise DeserializationError("ListSessionsResponse.sessions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
