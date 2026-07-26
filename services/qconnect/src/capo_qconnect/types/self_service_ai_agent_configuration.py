"""Generated from Smithy shape ``com.amazonaws.qconnect#SelfServiceAIAgentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.association_configuration_list
    import capo_qconnect.types.uuid_with_qualifier


class SelfServiceAIAgentConfiguration(TypedDict, closed=True):
    self_service_pre_processing_ai_prompt_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Prompt identifier for the Self Service Pre-Processing prompt used by the SELF_SERVICE AI Agent</p>"""
    self_service_answer_generation_ai_prompt_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Prompt identifier for the Self Service Answer Generation prompt used by the SELF_SERVICE AI Agent</p>"""
    self_service_ai_guardrail_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Guardrail identifier used by the SELF_SERVICE AI Agent.</p>"""
    association_configurations: NotRequired[
        "capo_qconnect.types.association_configuration_list.AssociationConfigurationList"
    ]
    """<p>The association configurations for overriding behavior on this AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfServiceAIAgentConfiguration) -> dict:
    out: dict = {}
    if "self_service_pre_processing_ai_prompt_id" in value:
        out["selfServicePreProcessingAIPromptId"] = value[
            "self_service_pre_processing_ai_prompt_id"
        ]
    if "self_service_answer_generation_ai_prompt_id" in value:
        out["selfServiceAnswerGenerationAIPromptId"] = value[
            "self_service_answer_generation_ai_prompt_id"
        ]
    if "self_service_ai_guardrail_id" in value:
        out["selfServiceAIGuardrailId"] = value["self_service_ai_guardrail_id"]
    if "association_configurations" in value:
        import capo_qconnect.types.association_configuration_list

        out["associationConfigurations"] = (
            capo_qconnect.types.association_configuration_list.serialize_json(
                value["association_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelfServiceAIAgentConfiguration:
    out: SelfServiceAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if "selfServicePreProcessingAIPromptId" in data:
        out["self_service_pre_processing_ai_prompt_id"] = data[
            "selfServicePreProcessingAIPromptId"
        ]
    if "selfServiceAnswerGenerationAIPromptId" in data:
        out["self_service_answer_generation_ai_prompt_id"] = data[
            "selfServiceAnswerGenerationAIPromptId"
        ]
    if "selfServiceAIGuardrailId" in data:
        out["self_service_ai_guardrail_id"] = data["selfServiceAIGuardrailId"]
    if "associationConfigurations" in data:
        import capo_qconnect.types.association_configuration_list

        out["association_configurations"] = (
            capo_qconnect.types.association_configuration_list.deserialize_json(
                data["associationConfigurations"]
            )
        )
    return out
