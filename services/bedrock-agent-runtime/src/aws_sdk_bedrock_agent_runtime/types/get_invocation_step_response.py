"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetInvocationStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invocation_step


class GetInvocationStepResponse(TypedDict, closed=True):
    invocation_step: (
        "aws_sdk_bedrock_agent_runtime.types.invocation_step.InvocationStep"
    )
    """<p>The complete details of the requested invocation step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvocationStepResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.invocation_step

    out["invocationStep"] = (
        aws_sdk_bedrock_agent_runtime.types.invocation_step.serialize_json(
            value["invocation_step"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetInvocationStepResponse:
    out: GetInvocationStepResponse = {}  # type: ignore[typeddict-item]
    if "invocationStep" in data:
        import aws_sdk_bedrock_agent_runtime.types.invocation_step

        out["invocation_step"] = (
            aws_sdk_bedrock_agent_runtime.types.invocation_step.deserialize_json(
                data["invocationStep"]
            )
        )
    else:
        raise DeserializationError("GetInvocationStepResponse.invocation_step required")
    return out
