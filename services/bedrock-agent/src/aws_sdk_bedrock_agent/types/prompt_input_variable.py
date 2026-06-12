"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptInputVariable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.prompt_input_variable_name


class PromptInputVariable(TypedDict):
    name: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_input_variable_name.PromptInputVariableName"
    ]
    """<p>The name of the variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptInputVariable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> PromptInputVariable:
    out: PromptInputVariable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
