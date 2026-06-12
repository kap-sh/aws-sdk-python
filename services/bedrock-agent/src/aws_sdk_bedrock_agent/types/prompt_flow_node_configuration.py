"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.guardrail_configuration
    import aws_sdk_bedrock_agent.types.prompt_flow_node_source_configuration


class PromptFlowNodeConfiguration(TypedDict):
    source_configuration: "aws_sdk_bedrock_agent.types.prompt_flow_node_source_configuration.PromptFlowNodeSourceConfiguration"
    """<p>Specifies whether the prompt is from Prompt management or defined inline.</p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Contains configurations for a guardrail to apply to the prompt in this node and the response generated from it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptFlowNodeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.prompt_flow_node_source_configuration

    out["sourceConfiguration"] = (
        aws_sdk_bedrock_agent.types.prompt_flow_node_source_configuration.serialize_json(
            value["source_configuration"]
        )
    )
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PromptFlowNodeConfiguration:
    out: PromptFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.prompt_flow_node_source_configuration

        out["source_configuration"] = (
            aws_sdk_bedrock_agent.types.prompt_flow_node_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PromptFlowNodeConfiguration.source_configuration required"
        )
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrail_configuration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    return out
