"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptFlowNodeResourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_prompt_arn


class PromptFlowNodeResourceConfiguration(TypedDict, closed=True):
    prompt_arn: "aws_sdk_bedrock_agent.types.flow_prompt_arn.FlowPromptArn"
    """<p>The Amazon Resource Name (ARN) of the prompt from Prompt management.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptFlowNodeResourceConfiguration) -> dict:
    out: dict = {}
    out["promptArn"] = value.get("prompt_arn", "")
    return out


def deserialize_json(data: dict) -> PromptFlowNodeResourceConfiguration:
    out: PromptFlowNodeResourceConfiguration = {}  # type: ignore[typeddict-item]
    if "promptArn" in data:
        out["prompt_arn"] = data["promptArn"]
    else:
        out["prompt_arn"] = ""
    return out
