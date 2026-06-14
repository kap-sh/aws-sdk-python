"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteCodeInterpreterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_id


class DeleteCodeInterpreterRequest(TypedDict):
    code_interpreter_id: (
        "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    )
    """<p>The unique identifier of the code interpreter to delete.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeInterpreterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCodeInterpreterRequest:
    out: DeleteCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
    return out
