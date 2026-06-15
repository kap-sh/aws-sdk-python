"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionTextInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.tool_description_list


class ToolDescriptionTextInput(TypedDict):
    tools: "aws_sdk_bedrock_agentcore.types.tool_description_list.ToolDescriptionList"
    """<p>The list of tool descriptions to optimize.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionTextInput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.tool_description_list

    out["tools"] = aws_sdk_bedrock_agentcore.types.tool_description_list.serialize_json(
        value["tools"]
    )
    return out


def deserialize_json(data: dict) -> ToolDescriptionTextInput:
    out: ToolDescriptionTextInput = {}  # type: ignore[typeddict-item]
    if "tools" in data:
        import aws_sdk_bedrock_agentcore.types.tool_description_list

        out["tools"] = (
            aws_sdk_bedrock_agentcore.types.tool_description_list.deserialize_json(
                data["tools"]
            )
        )
    else:
        raise DeserializationError("ToolDescriptionTextInput.tools required")
    return out
