"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedToolsDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.tools_definition


class UpdatedToolsDefinition(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.tools_definition.ToolsDefinition"
    ]
    """<p>The updated tools definition value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedToolsDefinition) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.tools_definition

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.tools_definition.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedToolsDefinition:
    out: UpdatedToolsDefinition = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import capo_bedrock_agentcore_control.types.tools_definition

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.tools_definition.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
