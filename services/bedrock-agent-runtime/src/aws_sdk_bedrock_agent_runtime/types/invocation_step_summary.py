"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationStepSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.uuid


class InvocationStepSummary(TypedDict):
    session_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the session associated with the invocation step.</p>"""
    invocation_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>A unique identifier for the invocation in UUID format.</p>"""
    invocation_step_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier (in UUID format) for the invocation step.</p>"""
    invocation_step_time: (
        "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp for when the invocation step was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationStepSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["invocationId"] = value["invocation_id"]
    out["invocationStepId"] = value["invocation_step_id"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["invocationStepTime"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["invocation_step_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvocationStepSummary:
    out: InvocationStepSummary = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("InvocationStepSummary.session_id required")
    if "invocationId" in data:
        out["invocation_id"] = data["invocationId"]
    else:
        raise DeserializationError("InvocationStepSummary.invocation_id required")
    if "invocationStepId" in data:
        out["invocation_step_id"] = data["invocationStepId"]
    else:
        raise DeserializationError("InvocationStepSummary.invocation_step_id required")
    if "invocationStepTime" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["invocation_step_time"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["invocationStepTime"]
            )
        )
    else:
        raise DeserializationError(
            "InvocationStepSummary.invocation_step_time required"
        )
    return out
