"""Generated from Smithy shape ``com.amazonaws.qconnect#OrchestrationAIAgentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.generic_arn
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.tool_configuration_list
    import aws_sdk_qconnect.types.uuid_with_qualifier


class OrchestrationAIAgentConfiguration(TypedDict):
    orchestration_ai_prompt_id: (
        "aws_sdk_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    )
    """<p>The AI Prompt identifier used by the Orchestration AI Agent.</p>"""
    orchestration_ai_guardrail_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Guardrail identifier used by the Orchestration AI Agent.</p>"""
    tool_configurations: NotRequired[
        "aws_sdk_qconnect.types.tool_configuration_list.ToolConfigurationList"
    ]
    """<p>The tool configurations used by the Orchestration AI Agent.</p>"""
    connect_instance_arn: NotRequired["aws_sdk_qconnect.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Connect instance used by the Orchestration AI Agent.</p>"""
    locale: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The locale setting for the Orchestration AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationAIAgentConfiguration) -> dict:
    out: dict = {}
    out["orchestrationAIPromptId"] = value["orchestration_ai_prompt_id"]
    if "orchestration_ai_guardrail_id" in value:
        out["orchestrationAIGuardrailId"] = value["orchestration_ai_guardrail_id"]
    if "tool_configurations" in value:
        import aws_sdk_qconnect.types.tool_configuration_list

        out["toolConfigurations"] = (
            aws_sdk_qconnect.types.tool_configuration_list.serialize_json(
                value["tool_configurations"]
            )
        )
    if "connect_instance_arn" in value:
        out["connectInstanceArn"] = value["connect_instance_arn"]
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_json(data: dict) -> OrchestrationAIAgentConfiguration:
    out: OrchestrationAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if "orchestrationAIPromptId" in data:
        out["orchestration_ai_prompt_id"] = data["orchestrationAIPromptId"]
    else:
        raise DeserializationError(
            "OrchestrationAIAgentConfiguration.orchestration_ai_prompt_id required"
        )
    if "orchestrationAIGuardrailId" in data:
        out["orchestration_ai_guardrail_id"] = data["orchestrationAIGuardrailId"]
    if "toolConfigurations" in data:
        import aws_sdk_qconnect.types.tool_configuration_list

        out["tool_configurations"] = (
            aws_sdk_qconnect.types.tool_configuration_list.deserialize_json(
                data["toolConfigurations"]
            )
        )
    if "connectInstanceArn" in data:
        out["connect_instance_arn"] = data["connectInstanceArn"]
    if "locale" in data:
        out["locale"] = data["locale"]
    return out
