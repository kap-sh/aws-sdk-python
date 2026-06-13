"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineAgentReturnControlPayload``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invocation_inputs


class InlineAgentReturnControlPayload(TypedDict):
    invocation_inputs: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.invocation_inputs.InvocationInputs"
    ]
    """<p>A list of objects that contain information about the parameters and inputs that need to be sent into the API operation or function, based on what the agent determines from its session with the user.</p>"""
    invocation_id: NotRequired["str"]
    """<p>The identifier of the action group invocation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineAgentReturnControlPayload) -> dict:
    out: dict = {}
    if "invocation_inputs" in value:
        import aws_sdk_bedrock_agent_runtime.types.invocation_inputs

        out["invocationInputs"] = (
            aws_sdk_bedrock_agent_runtime.types.invocation_inputs.serialize_json(
                value["invocation_inputs"]
            )
        )
    if "invocation_id" in value:
        out["invocationId"] = value["invocation_id"]
    return out


def deserialize_json(data: dict) -> InlineAgentReturnControlPayload:
    out: InlineAgentReturnControlPayload = {}  # type: ignore[typeddict-item]
    if "invocationInputs" in data:
        import aws_sdk_bedrock_agent_runtime.types.invocation_inputs

        out["invocation_inputs"] = (
            aws_sdk_bedrock_agent_runtime.types.invocation_inputs.deserialize_json(
                data["invocationInputs"]
            )
        )
    if "invocationId" in data:
        out["invocation_id"] = data["invocationId"]
    return out
