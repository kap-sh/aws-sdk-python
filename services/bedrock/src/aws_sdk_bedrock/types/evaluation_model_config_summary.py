"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationModelConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_bedrock_model_identifiers
    import aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifiers


class EvaluationModelConfigSummary(TypedDict, closed=True):
    bedrock_model_identifiers: NotRequired[
        "aws_sdk_bedrock.types.evaluation_bedrock_model_identifiers.EvaluationBedrockModelIdentifiers"
    ]
    """<p>The Amazon Resource Names (ARNs) of the models used for the evaluation job.</p>"""
    precomputed_inference_source_identifiers: NotRequired[
        "aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifiers.EvaluationPrecomputedInferenceSourceIdentifiers"
    ]
    """<p>A label that identifies the models used for a model evaluation job where you provide your own inference response data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationModelConfigSummary) -> dict:
    out: dict = {}
    if "bedrock_model_identifiers" in value:
        import aws_sdk_bedrock.types.evaluation_bedrock_model_identifiers

        out["bedrockModelIdentifiers"] = (
            aws_sdk_bedrock.types.evaluation_bedrock_model_identifiers.serialize_json(
                value["bedrock_model_identifiers"]
            )
        )
    if "precomputed_inference_source_identifiers" in value:
        import aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifiers

        out["precomputedInferenceSourceIdentifiers"] = (
            aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifiers.serialize_json(
                value["precomputed_inference_source_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationModelConfigSummary:
    out: EvaluationModelConfigSummary = {}  # type: ignore[typeddict-item]
    if "bedrockModelIdentifiers" in data:
        import aws_sdk_bedrock.types.evaluation_bedrock_model_identifiers

        out["bedrock_model_identifiers"] = (
            aws_sdk_bedrock.types.evaluation_bedrock_model_identifiers.deserialize_json(
                data["bedrockModelIdentifiers"]
            )
        )
    if "precomputedInferenceSourceIdentifiers" in data:
        import aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifiers

        out["precomputed_inference_source_identifiers"] = (
            aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifiers.deserialize_json(
                data["precomputedInferenceSourceIdentifiers"]
            )
        )
    return out
