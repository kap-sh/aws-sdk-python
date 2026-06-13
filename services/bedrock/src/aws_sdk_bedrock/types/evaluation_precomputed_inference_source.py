"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationPrecomputedInferenceSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifier


class EvaluationPrecomputedInferenceSource(TypedDict):
    inference_source_identifier: "aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifier.EvaluationPrecomputedInferenceSourceIdentifier"
    """<p>A label that identifies a model used in a model evaluation job where you provide your own inference response data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationPrecomputedInferenceSource) -> dict:
    out: dict = {}
    out["inferenceSourceIdentifier"] = value["inference_source_identifier"]
    return out


def deserialize_json(data: dict) -> EvaluationPrecomputedInferenceSource:
    out: EvaluationPrecomputedInferenceSource = {}  # type: ignore[typeddict-item]
    if "inferenceSourceIdentifier" in data:
        out["inference_source_identifier"] = data["inferenceSourceIdentifier"]
    else:
        raise DeserializationError(
            "EvaluationPrecomputedInferenceSource.inference_source_identifier required"
        )
    return out
