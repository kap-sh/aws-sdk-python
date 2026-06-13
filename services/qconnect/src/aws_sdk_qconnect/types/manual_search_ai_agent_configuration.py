"""Generated from Smithy shape ``com.amazonaws.qconnect#ManualSearchAIAgentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.association_configuration_list
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.uuid_with_qualifier


class ManualSearchAIAgentConfiguration(TypedDict):
    answer_generation_ai_prompt_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Prompt identifier for the Answer Generation prompt used by the MANUAL_SEARCH AI Agent.</p>"""
    answer_generation_ai_guardrail_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Guardrail identifier for the Answer Generation guardrail used by the MANUAL_SEARCH AI Agent.</p>"""
    association_configurations: NotRequired[
        "aws_sdk_qconnect.types.association_configuration_list.AssociationConfigurationList"
    ]
    """<p>The association configurations for overriding behavior on this AI Agent.</p>"""
    locale: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The locale to which specifies the language and region settings that determine the response language for <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html\">QueryAssistant</a>.</p> <note> <p>For more information on supported locales, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html#qic-notes-languages\">Language support for Amazon Q in Connect</a>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManualSearchAIAgentConfiguration) -> dict:
    out: dict = {}
    if "answer_generation_ai_prompt_id" in value:
        out["answerGenerationAIPromptId"] = value["answer_generation_ai_prompt_id"]
    if "answer_generation_ai_guardrail_id" in value:
        out["answerGenerationAIGuardrailId"] = value[
            "answer_generation_ai_guardrail_id"
        ]
    if "association_configurations" in value:
        import aws_sdk_qconnect.types.association_configuration_list

        out["associationConfigurations"] = (
            aws_sdk_qconnect.types.association_configuration_list.serialize_json(
                value["association_configurations"]
            )
        )
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_json(data: dict) -> ManualSearchAIAgentConfiguration:
    out: ManualSearchAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if "answerGenerationAIPromptId" in data:
        out["answer_generation_ai_prompt_id"] = data["answerGenerationAIPromptId"]
    if "answerGenerationAIGuardrailId" in data:
        out["answer_generation_ai_guardrail_id"] = data["answerGenerationAIGuardrailId"]
    if "associationConfigurations" in data:
        import aws_sdk_qconnect.types.association_configuration_list

        out["association_configurations"] = (
            aws_sdk_qconnect.types.association_configuration_list.deserialize_json(
                data["associationConfigurations"]
            )
        )
    if "locale" in data:
        out["locale"] = data["locale"]
    return out
