"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.answer_recommendation_ai_agent_configuration
    import aws_sdk_qconnect.types.case_summarization_ai_agent_configuration
    import aws_sdk_qconnect.types.email_generative_answer_ai_agent_configuration
    import aws_sdk_qconnect.types.email_overview_ai_agent_configuration
    import aws_sdk_qconnect.types.email_response_ai_agent_configuration
    import aws_sdk_qconnect.types.manual_search_ai_agent_configuration
    import aws_sdk_qconnect.types.note_taking_ai_agent_configuration
    import aws_sdk_qconnect.types.orchestration_ai_agent_configuration
    import aws_sdk_qconnect.types.self_service_ai_agent_configuration


class _AIAgentConfiguration_manualSearchAIAgentConfiguration(TypedDict):
    manualSearchAIAgentConfiguration: "aws_sdk_qconnect.types.manual_search_ai_agent_configuration.ManualSearchAIAgentConfiguration"


class _AIAgentConfiguration_answerRecommendationAIAgentConfiguration(TypedDict):
    answerRecommendationAIAgentConfiguration: "aws_sdk_qconnect.types.answer_recommendation_ai_agent_configuration.AnswerRecommendationAIAgentConfiguration"


class _AIAgentConfiguration_selfServiceAIAgentConfiguration(TypedDict):
    selfServiceAIAgentConfiguration: "aws_sdk_qconnect.types.self_service_ai_agent_configuration.SelfServiceAIAgentConfiguration"


class _AIAgentConfiguration_emailResponseAIAgentConfiguration(TypedDict):
    emailResponseAIAgentConfiguration: "aws_sdk_qconnect.types.email_response_ai_agent_configuration.EmailResponseAIAgentConfiguration"


class _AIAgentConfiguration_emailOverviewAIAgentConfiguration(TypedDict):
    emailOverviewAIAgentConfiguration: "aws_sdk_qconnect.types.email_overview_ai_agent_configuration.EmailOverviewAIAgentConfiguration"


class _AIAgentConfiguration_emailGenerativeAnswerAIAgentConfiguration(TypedDict):
    emailGenerativeAnswerAIAgentConfiguration: "aws_sdk_qconnect.types.email_generative_answer_ai_agent_configuration.EmailGenerativeAnswerAIAgentConfiguration"


class _AIAgentConfiguration_orchestrationAIAgentConfiguration(TypedDict):
    orchestrationAIAgentConfiguration: "aws_sdk_qconnect.types.orchestration_ai_agent_configuration.OrchestrationAIAgentConfiguration"


class _AIAgentConfiguration_noteTakingAIAgentConfiguration(TypedDict):
    noteTakingAIAgentConfiguration: "aws_sdk_qconnect.types.note_taking_ai_agent_configuration.NoteTakingAIAgentConfiguration"


class _AIAgentConfiguration_caseSummarizationAIAgentConfiguration(TypedDict):
    caseSummarizationAIAgentConfiguration: "aws_sdk_qconnect.types.case_summarization_ai_agent_configuration.CaseSummarizationAIAgentConfiguration"


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
        import aws_sdk_qconnect.types.manual_search_ai_agent_configuration

        return {
            "manualSearchAIAgentConfiguration": aws_sdk_qconnect.types.manual_search_ai_agent_configuration.serialize_json(
                value["manualSearchAIAgentConfiguration"]
            )
        }
    elif "answerRecommendationAIAgentConfiguration" in value:
        import aws_sdk_qconnect.types.answer_recommendation_ai_agent_configuration

        return {
            "answerRecommendationAIAgentConfiguration": aws_sdk_qconnect.types.answer_recommendation_ai_agent_configuration.serialize_json(
                value["answerRecommendationAIAgentConfiguration"]
            )
        }
    elif "selfServiceAIAgentConfiguration" in value:
        import aws_sdk_qconnect.types.self_service_ai_agent_configuration

        return {
            "selfServiceAIAgentConfiguration": aws_sdk_qconnect.types.self_service_ai_agent_configuration.serialize_json(
                value["selfServiceAIAgentConfiguration"]
            )
        }
    elif "emailResponseAIAgentConfiguration" in value:
        import aws_sdk_qconnect.types.email_response_ai_agent_configuration

        return {
            "emailResponseAIAgentConfiguration": aws_sdk_qconnect.types.email_response_ai_agent_configuration.serialize_json(
                value["emailResponseAIAgentConfiguration"]
            )
        }
    elif "emailOverviewAIAgentConfiguration" in value:
        import aws_sdk_qconnect.types.email_overview_ai_agent_configuration

        return {
            "emailOverviewAIAgentConfiguration": aws_sdk_qconnect.types.email_overview_ai_agent_configuration.serialize_json(
                value["emailOverviewAIAgentConfiguration"]
            )
        }
    elif "emailGenerativeAnswerAIAgentConfiguration" in value:
        import aws_sdk_qconnect.types.email_generative_answer_ai_agent_configuration

        return {
            "emailGenerativeAnswerAIAgentConfiguration": aws_sdk_qconnect.types.email_generative_answer_ai_agent_configuration.serialize_json(
                value["emailGenerativeAnswerAIAgentConfiguration"]
            )
        }
    elif "orchestrationAIAgentConfiguration" in value:
        import aws_sdk_qconnect.types.orchestration_ai_agent_configuration

        return {
            "orchestrationAIAgentConfiguration": aws_sdk_qconnect.types.orchestration_ai_agent_configuration.serialize_json(
                value["orchestrationAIAgentConfiguration"]
            )
        }
    elif "noteTakingAIAgentConfiguration" in value:
        import aws_sdk_qconnect.types.note_taking_ai_agent_configuration

        return {
            "noteTakingAIAgentConfiguration": aws_sdk_qconnect.types.note_taking_ai_agent_configuration.serialize_json(
                value["noteTakingAIAgentConfiguration"]
            )
        }
    elif "caseSummarizationAIAgentConfiguration" in value:
        import aws_sdk_qconnect.types.case_summarization_ai_agent_configuration

        return {
            "caseSummarizationAIAgentConfiguration": aws_sdk_qconnect.types.case_summarization_ai_agent_configuration.serialize_json(
                value["caseSummarizationAIAgentConfiguration"]
            )
        }
    else:
        raise SerializationError("AIAgentConfiguration: no variant present")


def deserialize_json(data: dict) -> AIAgentConfiguration:
    if "manualSearchAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.manual_search_ai_agent_configuration

        return {
            "manualSearchAIAgentConfiguration": aws_sdk_qconnect.types.manual_search_ai_agent_configuration.deserialize_json(
                data["manualSearchAIAgentConfiguration"]
            )
        }
    elif "answerRecommendationAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.answer_recommendation_ai_agent_configuration

        return {
            "answerRecommendationAIAgentConfiguration": aws_sdk_qconnect.types.answer_recommendation_ai_agent_configuration.deserialize_json(
                data["answerRecommendationAIAgentConfiguration"]
            )
        }
    elif "selfServiceAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.self_service_ai_agent_configuration

        return {
            "selfServiceAIAgentConfiguration": aws_sdk_qconnect.types.self_service_ai_agent_configuration.deserialize_json(
                data["selfServiceAIAgentConfiguration"]
            )
        }
    elif "emailResponseAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.email_response_ai_agent_configuration

        return {
            "emailResponseAIAgentConfiguration": aws_sdk_qconnect.types.email_response_ai_agent_configuration.deserialize_json(
                data["emailResponseAIAgentConfiguration"]
            )
        }
    elif "emailOverviewAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.email_overview_ai_agent_configuration

        return {
            "emailOverviewAIAgentConfiguration": aws_sdk_qconnect.types.email_overview_ai_agent_configuration.deserialize_json(
                data["emailOverviewAIAgentConfiguration"]
            )
        }
    elif "emailGenerativeAnswerAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.email_generative_answer_ai_agent_configuration

        return {
            "emailGenerativeAnswerAIAgentConfiguration": aws_sdk_qconnect.types.email_generative_answer_ai_agent_configuration.deserialize_json(
                data["emailGenerativeAnswerAIAgentConfiguration"]
            )
        }
    elif "orchestrationAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.orchestration_ai_agent_configuration

        return {
            "orchestrationAIAgentConfiguration": aws_sdk_qconnect.types.orchestration_ai_agent_configuration.deserialize_json(
                data["orchestrationAIAgentConfiguration"]
            )
        }
    elif "noteTakingAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.note_taking_ai_agent_configuration

        return {
            "noteTakingAIAgentConfiguration": aws_sdk_qconnect.types.note_taking_ai_agent_configuration.deserialize_json(
                data["noteTakingAIAgentConfiguration"]
            )
        }
    elif "caseSummarizationAIAgentConfiguration" in data:
        import aws_sdk_qconnect.types.case_summarization_ai_agent_configuration

        return {
            "caseSummarizationAIAgentConfiguration": aws_sdk_qconnect.types.case_summarization_ai_agent_configuration.deserialize_json(
                data["caseSummarizationAIAgentConfiguration"]
            )
        }
    else:
        raise DeserializationError("AIAgentConfiguration: no recognized variant key")
