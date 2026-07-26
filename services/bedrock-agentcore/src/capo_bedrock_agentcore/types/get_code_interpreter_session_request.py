"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetCodeInterpreterSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.code_interpreter_session_id


class GetCodeInterpreterSessionRequest(TypedDict, closed=True):
    code_interpreter_identifier: "str"
    """<p>The unique identifier of the code interpreter associated with the session.</p>"""
    session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    """<p>The unique identifier of the code interpreter session to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeInterpreterSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeInterpreterSessionRequest:
    out: GetCodeInterpreterSessionRequest = {}  # type: ignore[typeddict-item]
    return out
