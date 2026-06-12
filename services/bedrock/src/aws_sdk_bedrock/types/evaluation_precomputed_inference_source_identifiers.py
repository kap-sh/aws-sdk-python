"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationPrecomputedInferenceSourceIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifier

EvaluationPrecomputedInferenceSourceIdentifiers: TypeAlias = list[
    "aws_sdk_bedrock.types.evaluation_precomputed_inference_source_identifier.EvaluationPrecomputedInferenceSourceIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationPrecomputedInferenceSourceIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationPrecomputedInferenceSourceIdentifiers:
    return list(data)
