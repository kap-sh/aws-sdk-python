"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationInferenceConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_model_config_summary
    import capo_bedrock.types.evaluation_rag_config_summary


class EvaluationInferenceConfigSummary(TypedDict, closed=True):
    model_config_summary: NotRequired[
        "capo_bedrock.types.evaluation_model_config_summary.EvaluationModelConfigSummary"
    ]
    """<p>A summary of the models used in an Amazon Bedrock model evaluation job. These resources can be models in Amazon Bedrock or models outside of Amazon Bedrock that you use to generate your own inference response data.</p>"""
    rag_config_summary: NotRequired[
        "capo_bedrock.types.evaluation_rag_config_summary.EvaluationRagConfigSummary"
    ]
    """<p>A summary of the RAG resources used in an Amazon Bedrock Knowledge Base evaluation job. These resources can be Knowledge Bases in Amazon Bedrock or RAG sources outside of Amazon Bedrock that you use to generate your own inference response data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationInferenceConfigSummary) -> dict:
    out: dict = {}
    if "model_config_summary" in value:
        import capo_bedrock.types.evaluation_model_config_summary

        out["modelConfigSummary"] = (
            capo_bedrock.types.evaluation_model_config_summary.serialize_json(
                value["model_config_summary"]
            )
        )
    if "rag_config_summary" in value:
        import capo_bedrock.types.evaluation_rag_config_summary

        out["ragConfigSummary"] = (
            capo_bedrock.types.evaluation_rag_config_summary.serialize_json(
                value["rag_config_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationInferenceConfigSummary:
    out: EvaluationInferenceConfigSummary = {}  # type: ignore[typeddict-item]
    if "modelConfigSummary" in data:
        import capo_bedrock.types.evaluation_model_config_summary

        out["model_config_summary"] = (
            capo_bedrock.types.evaluation_model_config_summary.deserialize_json(
                data["modelConfigSummary"]
            )
        )
    if "ragConfigSummary" in data:
        import capo_bedrock.types.evaluation_rag_config_summary

        out["rag_config_summary"] = (
            capo_bedrock.types.evaluation_rag_config_summary.deserialize_json(
                data["ragConfigSummary"]
            )
        )
    return out
