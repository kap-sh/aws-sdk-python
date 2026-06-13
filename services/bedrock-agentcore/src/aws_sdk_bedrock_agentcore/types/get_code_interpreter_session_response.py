"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetCodeInterpreterSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.certificates
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_id
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_status
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_timeout
    import aws_sdk_bedrock_agentcore.types.date_timestamp
    import aws_sdk_bedrock_agentcore.types.name

class GetCodeInterpreterSessionResponse(TypedDict):
    code_interpreter_identifier: "str"
    """<p>The identifier of the code interpreter.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    """<p>The identifier of the code interpreter session.</p>"""
    name: NotRequired["aws_sdk_bedrock_agentcore.types.name.Name"]
    """<p>The name of the code interpreter session.</p>"""
    created_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The time at which the code interpreter session was created.</p>"""
    session_timeout_seconds: NotRequired["aws_sdk_bedrock_agentcore.types.code_interpreter_session_timeout.CodeInterpreterSessionTimeout"]
    """<p>The timeout period for the code interpreter session in seconds.</p>"""
    status: NotRequired["aws_sdk_bedrock_agentcore.types.code_interpreter_session_status.CodeInterpreterSessionStatus"]
    """<p>The current status of the code interpreter session. Possible values include ACTIVE, STOPPING, and STOPPED.</p>"""
    certificates: NotRequired["aws_sdk_bedrock_agentcore.types.certificates.Certificates"]
    """<p>The list of certificates installed in the code interpreter session.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetCodeInterpreterSessionResponse) -> dict:
    out: dict = {}
    out["codeInterpreterIdentifier"] = value["code_interpreter_identifier"]
    out["sessionId"] = value["session_id"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(value["created_at"])
    if "session_timeout_seconds" in value:
        out["sessionTimeoutSeconds"] = value["session_timeout_seconds"]
    if "status" in value:
        import aws_sdk_bedrock_agentcore.types.code_interpreter_session_status
        out["status"] = aws_sdk_bedrock_agentcore.types.code_interpreter_session_status.serialize_json(value["status"])
    if "certificates" in value:
        import aws_sdk_bedrock_agentcore.types.certificates
        out["certificates"] = aws_sdk_bedrock_agentcore.types.certificates.serialize_json(value["certificates"])
    return out


def deserialize_json(data: dict) -> GetCodeInterpreterSessionResponse:
    out: GetCodeInterpreterSessionResponse = {}  # type: ignore[typeddict-item]
    if "codeInterpreterIdentifier" in data:
        out["code_interpreter_identifier"] = data["codeInterpreterIdentifier"]
    else:
        raise DeserializationError("GetCodeInterpreterSessionResponse.code_interpreter_identifier required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("GetCodeInterpreterSessionResponse.session_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("GetCodeInterpreterSessionResponse.created_at required")
    if "sessionTimeoutSeconds" in data:
        out["session_timeout_seconds"] = data["sessionTimeoutSeconds"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.code_interpreter_session_status
        out["status"] = aws_sdk_bedrock_agentcore.types.code_interpreter_session_status.deserialize_json(data["status"])
    if "certificates" in data:
        import aws_sdk_bedrock_agentcore.types.certificates
        out["certificates"] = aws_sdk_bedrock_agentcore.types.certificates.deserialize_json(data["certificates"])
    return out