"""Generated from Smithy shape ``com.amazonaws.qconnect#SearchSessionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.session_summaries


class SearchSessionsResponse(TypedDict):
    session_summaries: "aws_sdk_qconnect.types.session_summaries.SessionSummaries"
    """<p>Summary information about the sessions.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSessionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.session_summaries

    out["sessionSummaries"] = aws_sdk_qconnect.types.session_summaries.serialize_json(
        value["session_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchSessionsResponse:
    out: SearchSessionsResponse = {}  # type: ignore[typeddict-item]
    if "sessionSummaries" in data:
        import aws_sdk_qconnect.types.session_summaries

        out["session_summaries"] = (
            aws_sdk_qconnect.types.session_summaries.deserialize_json(
                data["sessionSummaries"]
            )
        )
    else:
        raise DeserializationError("SearchSessionsResponse.session_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
