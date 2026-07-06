"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListCodeInterpreterSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_summaries
    import aws_sdk_bedrock_agentcore.types.next_token


class ListCodeInterpreterSessionsResponse(TypedDict, closed=True):
    items: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_summaries.CodeInterpreterSessionSummaries"
    """<p>The list of code interpreter sessions that match the specified criteria.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agentcore.types.next_token.NextToken"]
    """<p>The token to use in a subsequent <code>ListCodeInterpreterSessions</code> request to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeInterpreterSessionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_summaries

    out["items"] = (
        aws_sdk_bedrock_agentcore.types.code_interpreter_session_summaries.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeInterpreterSessionsResponse:
    out: ListCodeInterpreterSessionsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_bedrock_agentcore.types.code_interpreter_session_summaries

        out["items"] = (
            aws_sdk_bedrock_agentcore.types.code_interpreter_session_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ListCodeInterpreterSessionsResponse.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
