"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_tool_configuration
    import aws_sdk_bedrock_agentcore_control.types.harness_tool_name
    import aws_sdk_bedrock_agentcore_control.types.harness_tool_type


class HarnessTool(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agentcore_control.types.harness_tool_type.HarnessToolType"
    """<p>The type of tool.</p>"""
    name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_tool_name.HarnessToolName"
    ]
    """<p>Unique name for the tool. If not provided, a name will be inferred or generated.</p>"""
    config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_tool_configuration.HarnessToolConfiguration"
    ]
    """<p>Tool-specific configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTool) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.harness_tool_type

    out["type"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_tool_type.serialize_json(
            value["type"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    if "config" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_tool_configuration

        out["config"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_tool_configuration.serialize_json(
                value["config"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessTool:
    out: HarnessTool = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_tool_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_tool_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("HarnessTool.type required")
    if "name" in data:
        out["name"] = data["name"]
    if "config" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_tool_configuration

        out["config"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_tool_configuration.deserialize_json(
                data["config"]
            )
        )
    return out
