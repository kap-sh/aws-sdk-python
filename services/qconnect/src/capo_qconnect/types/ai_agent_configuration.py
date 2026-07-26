"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.answer_recommendation_ai_agent_configuration
    import capo_qconnect.types.case_summarization_ai_agent_configuration
    import capo_qconnect.types.email_generative_answer_ai_agent_configuration
    import capo_qconnect.types.email_overview_ai_agent_configuration
    import capo_qconnect.types.email_response_ai_agent_configuration
    import capo_qconnect.types.manual_search_ai_agent_configuration
    import capo_qconnect.types.note_taking_ai_agent_configuration
    import capo_qconnect.types.orchestration_ai_agent_configuration
    import capo_qconnect.types.self_service_ai_agent_configuration


class _AIAgentConfiguration_manualSearchAIAgentConfiguration(TypedDict, closed=True):
    manualSearchAIAgentConfiguration: "capo_qconnect.types.manual_search_ai_agent_configuration.ManualSearchAIAgentConfiguration"


class _AIAgentConfiguration_answerRecommendationAIAgentConfiguration(
    TypedDict, closed=True
):
    answerRecommendationAIAgentConfiguration: "capo_qconnect.types.answer_recommendation_ai_agent_configuration.AnswerRecommendationAIAgentConfiguration"


class _AIAgentConfiguration_selfServiceAIAgentConfiguration(TypedDict, closed=True):
    selfServiceAIAgentConfiguration: "capo_qconnect.types.self_service_ai_agent_configuration.SelfServiceAIAgentConfiguration"


class _AIAgentConfiguration_emailResponseAIAgentConfiguration(TypedDict, closed=True):
    emailResponseAIAgentConfiguration: "capo_qconnect.types.email_response_ai_agent_configuration.EmailResponseAIAgentConfiguration"


class _AIAgentConfiguration_emailOverviewAIAgentConfiguration(TypedDict, closed=True):
    emailOverviewAIAgentConfiguration: "capo_qconnect.types.email_overview_ai_agent_configuration.EmailOverviewAIAgentConfiguration"


class _AIAgentConfiguration_emailGenerativeAnswerAIAgentConfiguration(
    TypedDict, closed=True
):
    emailGenerativeAnswerAIAgentConfiguration: "capo_qconnect.types.email_generative_answer_ai_agent_configuration.EmailGenerativeAnswerAIAgentConfiguration"


class _AIAgentConfiguration_orchestrationAIAgentConfiguration(TypedDict, closed=True):
    orchestrationAIAgentConfiguration: "capo_qconnect.types.orchestration_ai_agent_configuration.OrchestrationAIAgentConfiguration"


class _AIAgentConfiguration_noteTakingAIAgentConfiguration(TypedDict, closed=True):
    noteTakingAIAgentConfiguration: "capo_qconnect.types.note_taking_ai_agent_configuration.NoteTakingAIAgentConfiguration"


class _AIAgentConfiguration_caseSummarizationAIAgentConfiguration(
    TypedDict, closed=True
):
    caseSummarizationAIAgentConfiguration: "capo_qconnect.types.case_summarization_ai_agent_configuration.CaseSummarizationAIAgentConfiguration"


AIAgentConfiguration: TypeAlias = (
    _AIAgentConfiguration_manualSearchAIAgentConfiguration
    | _AIAgentConfiguration_answerRecommendationAIAgentConfiguration
    | _AIAgentConfiguration_selfServiceAIAgentConfiguration
    | _AIAgentConfiguration_emailResponseAIAgentConfiguration
    | _AIAgentConfiguration_emailOverviewAIAgentConfiguration
    | _AIAgentConfiguration_emailGenerativeAnswerAIAgentConfiguration
    | _AIAgentConfiguration_orchestrationAIAgentConfiguration
    | _AIAgentConfiguration_noteTakingAIAgentConfiguration
    | _AIAgentConfiguration_caseSummarizationAIAgentConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentConfiguration) -> dict:
    if "manualSearchAIAgentConfiguration" in value:
        import capo_qconnect.types.manual_search_ai_agent_configuration

        return {
            "manualSearchAIAgentConfiguration": capo_qconnect.types.manual_search_ai_agent_configuration.serialize_json(
                value["manualSearchAIAgentConfiguration"]
            )
        }
    elif "answerRecommendationAIAgentConfiguration" in value:
        import capo_qconnect.types.answer_recommendation_ai_agent_configuration

        return {
            "answerRecommendationAIAgentConfiguration": capo_qconnect.types.answer_recommendation_ai_agent_configuration.serialize_json(
                value["answerRecommendationAIAgentConfiguration"]
            )
        }
    elif "selfServiceAIAgentConfiguration" in value:
        import capo_qconnect.types.self_service_ai_agent_configuration

        return {
            "selfServiceAIAgentConfiguration": capo_qconnect.types.self_service_ai_agent_configuration.serialize_json(
                value["selfServiceAIAgentConfiguration"]
            )
        }
    elif "emailResponseAIAgentConfiguration" in value:
        import capo_qconnect.types.email_response_ai_agent_configuration

        return {
            "emailResponseAIAgentConfiguration": capo_qconnect.types.email_response_ai_agent_configuration.serialize_json(
                value["emailResponseAIAgentConfiguration"]
            )
        }
    elif "emailOverviewAIAgentConfiguration" in value:
        import capo_qconnect.types.email_overview_ai_agent_configuration

        return {
            "emailOverviewAIAgentConfiguration": capo_qconnect.types.email_overview_ai_agent_configuration.serialize_json(
                value["emailOverviewAIAgentConfiguration"]
            )
        }
    elif "emailGenerativeAnswerAIAgentConfiguration" in value:
        import capo_qconnect.types.email_generative_answer_ai_agent_configuration

        return {
            "emailGenerativeAnswerAIAgentConfiguration": capo_qconnect.types.email_generative_answer_ai_agent_configuration.serialize_json(
                value["emailGenerativeAnswerAIAgentConfiguration"]
            )
        }
    elif "orchestrationAIAgentConfiguration" in value:
        import capo_qconnect.types.orchestration_ai_agent_configuration

        return {
            "orchestrationAIAgentConfiguration": capo_qconnect.types.orchestration_ai_agent_configuration.serialize_json(
                value["orchestrationAIAgentConfiguration"]
            )
        }
    elif "noteTakingAIAgentConfiguration" in value:
        import capo_qconnect.types.note_taking_ai_agent_configuration

        return {
            "noteTakingAIAgentConfiguration": capo_qconnect.types.note_taking_ai_agent_configuration.serialize_json(
                value["noteTakingAIAgentConfiguration"]
            )
        }
    elif "caseSummarizationAIAgentConfiguration" in value:
        import capo_qconnect.types.case_summarization_ai_agent_configuration

        return {
            "caseSummarizationAIAgentConfiguration": capo_qconnect.types.case_summarization_ai_agent_configuration.serialize_json(
                value["caseSummarizationAIAgentConfiguration"]
            )
        }
    else:
        raise SerializationError("AIAgentConfiguration: no variant present")


def deserialize_json(data: dict) -> AIAgentConfiguration:
    if "manualSearchAIAgentConfiguration" in data:
        import capo_qconnect.types.manual_search_ai_agent_configuration

        return {
            "manualSearchAIAgentConfiguration": capo_qconnect.types.manual_search_ai_agent_configuration.deserialize_json(
                data["manualSearchAIAgentConfiguration"]
            )
        }
    elif "answerRecommendationAIAgentConfiguration" in data:
        import capo_qconnect.types.answer_recommendation_ai_agent_configuration

        return {
            "answerRecommendationAIAgentConfiguration": capo_qconnect.types.answer_recommendation_ai_agent_configuration.deserialize_json(
                data["answerRecommendationAIAgentConfiguration"]
            )
        }
    elif "selfServiceAIAgentConfiguration" in data:
        import capo_qconnect.types.self_service_ai_agent_configuration

        return {
            "selfServiceAIAgentConfiguration": capo_qconnect.types.self_service_ai_agent_configuration.deserialize_json(
                data["selfServiceAIAgentConfiguration"]
            )
        }
    elif "emailResponseAIAgentConfiguration" in data:
        import capo_qconnect.types.email_response_ai_agent_configuration

        return {
            "emailResponseAIAgentConfiguration": capo_qconnect.types.email_response_ai_agent_configuration.deserialize_json(
                data["emailResponseAIAgentConfiguration"]
            )
        }
    elif "emailOverviewAIAgentConfiguration" in data:
        import capo_qconnect.types.email_overview_ai_agent_configuration

        return {
            "emailOverviewAIAgentConfiguration": capo_qconnect.types.email_overview_ai_agent_configuration.deserialize_json(
                data["emailOverviewAIAgentConfiguration"]
            )
        }
    elif "emailGenerativeAnswerAIAgentConfiguration" in data:
        import capo_qconnect.types.email_generative_answer_ai_agent_configuration

        return {
            "emailGenerativeAnswerAIAgentConfiguration": capo_qconnect.types.email_generative_answer_ai_agent_configuration.deserialize_json(
                data["emailGenerativeAnswerAIAgentConfiguration"]
            )
        }
    elif "orchestrationAIAgentConfiguration" in data:
        import capo_qconnect.types.orchestration_ai_agent_configuration

        return {
            "orchestrationAIAgentConfiguration": capo_qconnect.types.orchestration_ai_agent_configuration.deserialize_json(
                data["orchestrationAIAgentConfiguration"]
            )
        }
    elif "noteTakingAIAgentConfiguration" in data:
        import capo_qconnect.types.note_taking_ai_agent_configuration

        return {
            "noteTakingAIAgentConfiguration": capo_qconnect.types.note_taking_ai_agent_configuration.deserialize_json(
                data["noteTakingAIAgentConfiguration"]
            )
        }
    elif "caseSummarizationAIAgentConfiguration" in data:
        import capo_qconnect.types.case_summarization_ai_agent_configuration

        return {
            "caseSummarizationAIAgentConfiguration": capo_qconnect.types.case_summarization_ai_agent_configuration.deserialize_json(
                data["caseSummarizationAIAgentConfiguration"]
            )
        }
    else:
        raise DeserializationError("AIAgentConfiguration: no recognized variant key")
