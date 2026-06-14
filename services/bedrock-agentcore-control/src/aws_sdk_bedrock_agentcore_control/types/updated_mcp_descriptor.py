"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedMcpDescriptor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor_fields


class UpdatedMcpDescriptor(TypedDict):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor_fields.UpdatedMcpDescriptorFields"
    ]
    """<p>The updated MCP descriptor fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedMcpDescriptor) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor_fields

        out["optionalValue"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor_fields.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedMcpDescriptor:
    out: UpdatedMcpDescriptor = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor_fields

        out["optional_value"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor_fields.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
