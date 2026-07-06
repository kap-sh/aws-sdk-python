"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopCodeInterpreterSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_id
    import aws_sdk_bedrock_agentcore.types.date_timestamp


class StopCodeInterpreterSessionResponse(TypedDict, closed=True):
    code_interpreter_identifier: "str"
    """<p>The identifier of the code interpreter.</p>"""
    session_id: "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    """<p>The identifier of the code interpreter session.</p>"""
    last_updated_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter session was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCodeInterpreterSessionResponse) -> dict:
    out: dict = {}
    out["codeInterpreterIdentifier"] = value["code_interpreter_identifier"]
    out["sessionId"] = value["session_id"]
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> StopCodeInterpreterSessionResponse:
    out: StopCodeInterpreterSessionResponse = {}  # type: ignore[typeddict-item]
    if "codeInterpreterIdentifier" in data:
        out["code_interpreter_identifier"] = data["codeInterpreterIdentifier"]
    else:
        raise DeserializationError(
            "StopCodeInterpreterSessionResponse.code_interpreter_identifier required"
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError(
            "StopCodeInterpreterSessionResponse.session_id required"
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "StopCodeInterpreterSessionResponse.last_updated_at required"
        )
    return out
