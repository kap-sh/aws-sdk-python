"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationStep``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.invocation_step_payload
    import aws_sdk_bedrock_agent_runtime.types.uuid


class InvocationStep(TypedDict):
    session_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier of the session containing the invocation step.</p>"""
    invocation_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier (in UUID format) for the invocation that includes the invocation step.</p>"""
    invocation_step_id: "aws_sdk_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier (in UUID format) for the invocation step.</p>"""
    invocation_step_time: (
        "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp for when the invocation step was created.</p>"""
    payload: "aws_sdk_bedrock_agent_runtime.types.invocation_step_payload.InvocationStepPayload"
    """<p>Payload content, such as text and images, for the invocation step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationStep) -> dict:
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
    import aws_sdk_bedrock_agent_runtime.types.invocation_step_payload

    out["payload"] = (
        aws_sdk_bedrock_agent_runtime.types.invocation_step_payload.serialize_json(
            value["payload"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvocationStep:
    out: InvocationStep = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("InvocationStep.session_id required")
    if "invocationId" in data:
        out["invocation_id"] = data["invocationId"]
    else:
        raise DeserializationError("InvocationStep.invocation_id required")
    if "invocationStepId" in data:
        out["invocation_step_id"] = data["invocationStepId"]
    else:
        raise DeserializationError("InvocationStep.invocation_step_id required")
    if "invocationStepTime" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["invocation_step_time"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["invocationStepTime"]
            )
        )
    else:
        raise DeserializationError("InvocationStep.invocation_step_time required")
    if "payload" in data:
        import aws_sdk_bedrock_agent_runtime.types.invocation_step_payload

        out["payload"] = (
            aws_sdk_bedrock_agent_runtime.types.invocation_step_payload.deserialize_json(
                data["payload"]
            )
        )
    else:
        raise DeserializationError("InvocationStep.payload required")
    return out
