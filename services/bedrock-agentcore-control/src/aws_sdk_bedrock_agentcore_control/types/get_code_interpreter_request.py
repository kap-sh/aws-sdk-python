"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetCodeInterpreterRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_id

class GetCodeInterpreterRequest(TypedDict):
    code_interpreter_id: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    """<p>The unique identifier of the code interpreter to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetCodeInterpreterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeInterpreterRequest:
    out: GetCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
    return out