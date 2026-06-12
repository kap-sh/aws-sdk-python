"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationQuestionAnswerAnalysisDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_contact_lens_answer_analysis_details
    import aws_sdk_connect.types.evaluation_gen_ai_answer_analysis_details


class _EvaluationQuestionAnswerAnalysisDetails_GenAI(TypedDict):
    GenAI: "aws_sdk_connect.types.evaluation_gen_ai_answer_analysis_details.EvaluationGenAIAnswerAnalysisDetails"


class _EvaluationQuestionAnswerAnalysisDetails_ContactLens(TypedDict):
    ContactLens: "aws_sdk_connect.types.evaluation_contact_lens_answer_analysis_details.EvaluationContactLensAnswerAnalysisDetails"


EvaluationQuestionAnswerAnalysisDetails: TypeAlias = (
    _EvaluationQuestionAnswerAnalysisDetails_GenAI
    | _EvaluationQuestionAnswerAnalysisDetails_ContactLens
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationQuestionAnswerAnalysisDetails) -> dict:
    if "GenAI" in value:
        import aws_sdk_connect.types.evaluation_gen_ai_answer_analysis_details

        return {
            "GenAI": aws_sdk_connect.types.evaluation_gen_ai_answer_analysis_details.serialize_json(
                value["GenAI"]
            )
        }
    elif "ContactLens" in value:
        import aws_sdk_connect.types.evaluation_contact_lens_answer_analysis_details

        return {
            "ContactLens": aws_sdk_connect.types.evaluation_contact_lens_answer_analysis_details.serialize_json(
                value["ContactLens"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationQuestionAnswerAnalysisDetails: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationQuestionAnswerAnalysisDetails:
    if "GenAI" in data:
        import aws_sdk_connect.types.evaluation_gen_ai_answer_analysis_details

        return {
            "GenAI": aws_sdk_connect.types.evaluation_gen_ai_answer_analysis_details.deserialize_json(
                data["GenAI"]
            )
        }
    elif "ContactLens" in data:
        import aws_sdk_connect.types.evaluation_contact_lens_answer_analysis_details

        return {
            "ContactLens": aws_sdk_connect.types.evaluation_contact_lens_answer_analysis_details.deserialize_json(
                data["ContactLens"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationQuestionAnswerAnalysisDetails: no recognized variant key"
        )
