"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartCodeInterpreterSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.code_interpreter_session_id
    import capo_bedrock_agentcore.types.date_timestamp


class StartCodeInterpreterSessionResponse(TypedDict, closed=True):
    code_interpreter_identifier: "str"
    """<p>The identifier of the code interpreter.</p>"""
    session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    """<p>The unique identifier of the created code interpreter session.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The time at which the code interpreter session was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeInterpreterSessionResponse) -> dict:
    out: dict = {}
    out["codeInterpreterIdentifier"] = value["code_interpreter_identifier"]
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> StartCodeInterpreterSessionResponse:
    out: StartCodeInterpreterSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("codeInterpreterIdentifier") is not None:
        out["code_interpreter_identifier"] = data["codeInterpreterIdentifier"]
    else:
        raise DeserializationError(
            "StartCodeInterpreterSessionResponse.code_interpreter_identifier required"
        )
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError(
            "StartCodeInterpreterSessionResponse.session_id required"
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError(
            "StartCodeInterpreterSessionResponse.created_at required"
        )
    return out
