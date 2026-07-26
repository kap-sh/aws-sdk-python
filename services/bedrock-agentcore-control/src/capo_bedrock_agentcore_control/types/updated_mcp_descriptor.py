"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedMcpDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.updated_mcp_descriptor_fields


class UpdatedMcpDescriptor(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_mcp_descriptor_fields.UpdatedMcpDescriptorFields"
    ]
    """<p>The updated MCP descriptor fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedMcpDescriptor) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.updated_mcp_descriptor_fields

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.updated_mcp_descriptor_fields.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedMcpDescriptor:
    out: UpdatedMcpDescriptor = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import capo_bedrock_agentcore_control.types.updated_mcp_descriptor_fields

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.updated_mcp_descriptor_fields.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
