"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetCodeInterpreterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_interpreter_id


class GetCodeInterpreterRequest(TypedDict, closed=True):
    code_interpreter_id: (
        "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    )
    """<p>The unique identifier of the code interpreter to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeInterpreterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeInterpreterRequest:
    out: GetCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
    return out
