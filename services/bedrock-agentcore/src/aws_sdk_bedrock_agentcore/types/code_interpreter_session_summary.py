"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterSessionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_id
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_status
    import aws_sdk_bedrock_agentcore.types.date_timestamp
    import aws_sdk_bedrock_agentcore.types.name


class CodeInterpreterSessionSummary(TypedDict):
    code_interpreter_identifier: "str"
    """<p>The unique identifier of the code interpreter associated with the session. This identifier specifies which code interpreter environment is used for the session.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    """<p>The unique identifier of the code interpreter session. This identifier is used in operations that interact with the session.</p>"""
    name: NotRequired["aws_sdk_bedrock_agentcore.types.name.Name"]
    """<p>The name of the code interpreter session. This name helps identify and manage the session.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_status.CodeInterpreterSessionStatus"
    """<p>The current status of the code interpreter session. Possible values include ACTIVE, STOPPING, and STOPPED.</p>"""
    created_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter session was created. This value is in ISO 8601 format.</p>"""
    last_updated_at: NotRequired[
        "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the code interpreter session was last updated. This value is in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterSessionSummary) -> dict:
    out: dict = {}
    out["codeInterpreterIdentifier"] = value["code_interpreter_identifier"]
    out["sessionId"] = value["session_id"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.code_interpreter_session_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "last_updated_at" in value:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeInterpreterSessionSummary:
    out: CodeInterpreterSessionSummary = {}  # type: ignore[typeddict-item]
    if "codeInterpreterIdentifier" in data:
        out["code_interpreter_identifier"] = data["codeInterpreterIdentifier"]
    else:
        raise DeserializationError(
            "CodeInterpreterSessionSummary.code_interpreter_identifier required"
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("CodeInterpreterSessionSummary.session_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.code_interpreter_session_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.code_interpreter_session_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CodeInterpreterSessionSummary.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CodeInterpreterSessionSummary.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
