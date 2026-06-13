"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SpecificToolChoice``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.tool_name


class SpecificToolChoice(TypedDict):
    name: "aws_sdk_bedrock_runtime.types.tool_name.ToolName"
    """<p>The name of the tool that the model must request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpecificToolChoice) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SpecificToolChoice:
    out: SpecificToolChoice = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SpecificToolChoice.name required")
    return out
