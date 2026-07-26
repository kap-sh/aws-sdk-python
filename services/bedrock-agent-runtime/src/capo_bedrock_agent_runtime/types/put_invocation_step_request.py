"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PutInvocationStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.invocation_identifier
    import capo_bedrock_agent_runtime.types.invocation_step_payload
    import capo_bedrock_agent_runtime.types.session_identifier
    import capo_bedrock_agent_runtime.types.uuid


class PutInvocationStepRequest(TypedDict, closed=True):
    session_identifier: (
        "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>The unique identifier for the session to add the invocation step to. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""
    invocation_identifier: (
        "capo_bedrock_agent_runtime.types.invocation_identifier.InvocationIdentifier"
    )
    """<p>The unique identifier (in UUID format) of the invocation to add the invocation step to.</p>"""
    invocation_step_time: (
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp for when the invocation step occurred.</p>"""
    payload: (
        "capo_bedrock_agent_runtime.types.invocation_step_payload.InvocationStepPayload"
    )
    """<p>The payload for the invocation step, including text and images for the interaction.</p>"""
    invocation_step_id: NotRequired["capo_bedrock_agent_runtime.types.uuid.Uuid"]
    """<p>The unique identifier of the invocation step in UUID format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutInvocationStepRequest) -> dict:
    out: dict = {}
    out["invocationIdentifier"] = value["invocation_identifier"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["invocationStepTime"] = (
        capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["invocation_step_time"]
        )
    )
    import capo_bedrock_agent_runtime.types.invocation_step_payload

    out["payload"] = (
        capo_bedrock_agent_runtime.types.invocation_step_payload.serialize_json(
            value["payload"]
        )
    )
    if "invocation_step_id" in value:
        out["invocationStepId"] = value["invocation_step_id"]
    return out


def deserialize_json(data: dict) -> PutInvocationStepRequest:
    out: PutInvocationStepRequest = {}  # type: ignore[typeddict-item]
    if "invocationIdentifier" in data:
        out["invocation_identifier"] = data["invocationIdentifier"]
    else:
        raise DeserializationError(
            "PutInvocationStepRequest.invocation_identifier required"
        )
    if "invocationStepTime" in data:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["invocation_step_time"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["invocationStepTime"]
            )
        )
    else:
        raise DeserializationError(
            "PutInvocationStepRequest.invocation_step_time required"
        )
    if "payload" in data:
        import capo_bedrock_agent_runtime.types.invocation_step_payload

        out["payload"] = (
            capo_bedrock_agent_runtime.types.invocation_step_payload.deserialize_json(
                data["payload"]
            )
        )
    else:
        raise DeserializationError("PutInvocationStepRequest.payload required")
    if "invocationStepId" in data:
        out["invocation_step_id"] = data["invocationStepId"]
    return out
