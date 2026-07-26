"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteCodeInterpreterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.code_interpreter_id


class DeleteCodeInterpreterRequest(TypedDict, closed=True):
    code_interpreter_id: (
        "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    )
    """<p>The unique identifier of the code interpreter to delete.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeInterpreterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCodeInterpreterRequest:
    out: DeleteCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
    return out
