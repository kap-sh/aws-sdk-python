"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreCodeInterpreterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_code_interpreter_arn


class HarnessAgentCoreCodeInterpreterConfig(TypedDict, closed=True):
    code_interpreter_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_code_interpreter_arn.HarnessCodeInterpreterArn"
    ]
    """<p>If not populated, the built-in Code Interpreter ARN is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreCodeInterpreterConfig) -> dict:
    out: dict = {}
    if "code_interpreter_arn" in value:
        out["codeInterpreterArn"] = value["code_interpreter_arn"]
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreCodeInterpreterConfig:
    out: HarnessAgentCoreCodeInterpreterConfig = {}  # type: ignore[typeddict-item]
    if "codeInterpreterArn" in data:
        out["code_interpreter_arn"] = data["codeInterpreterArn"]
    return out
