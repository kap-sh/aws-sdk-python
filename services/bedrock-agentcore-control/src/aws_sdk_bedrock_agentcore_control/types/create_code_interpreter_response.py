"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateCodeInterpreterResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_arn
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_id
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

class CreateCodeInterpreterResponse(TypedDict):
    code_interpreter_id: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    """<p>The unique identifier of the created code interpreter.</p>"""
    code_interpreter_arn: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_arn.CodeInterpreterArn"
    """<p>The Amazon Resource Name (ARN) of the created code interpreter.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter was created.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.CodeInterpreterStatus"
    """<p>The current status of the code interpreter.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeInterpreterResponse) -> dict:
    out: dict = {}
    out["codeInterpreterId"] = value["code_interpreter_id"]
    out["codeInterpreterArn"] = value["code_interpreter_arn"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["created_at"])
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateCodeInterpreterResponse:
    out: CreateCodeInterpreterResponse = {}  # type: ignore[typeddict-item]
    if "codeInterpreterId" in data:
        out["code_interpreter_id"] = data["codeInterpreterId"]
    else:
        raise DeserializationError("CreateCodeInterpreterResponse.code_interpreter_id required")
    if "codeInterpreterArn" in data:
        out["code_interpreter_arn"] = data["codeInterpreterArn"]
    else:
        raise DeserializationError("CreateCodeInterpreterResponse.code_interpreter_arn required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("CreateCodeInterpreterResponse.created_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateCodeInterpreterResponse.status required")
    return out