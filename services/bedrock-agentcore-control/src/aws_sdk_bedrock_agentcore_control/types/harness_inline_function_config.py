"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessInlineFunctionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_inline_function_description
    import aws_sdk_bedrock_agentcore_control.types.sensitive_json


class HarnessInlineFunctionConfig(TypedDict, closed=True):
    description: "aws_sdk_bedrock_agentcore_control.types.harness_inline_function_description.HarnessInlineFunctionDescription"
    """<p>Description of what the tool does, provided to the model.</p>"""
    input_schema: "aws_sdk_bedrock_agentcore_control.types.sensitive_json.SensitiveJson"
    """<p>JSON Schema describing the tool's input parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessInlineFunctionConfig) -> dict:
    out: dict = {}
    out["description"] = value["description"]
    out["inputSchema"] = value["input_schema"]
    return out


def deserialize_json(data: dict) -> HarnessInlineFunctionConfig:
    out: HarnessInlineFunctionConfig = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("HarnessInlineFunctionConfig.description required")
    if "inputSchema" in data:
        out["input_schema"] = data["inputSchema"]
    else:
        raise DeserializationError("HarnessInlineFunctionConfig.input_schema required")
    return out
