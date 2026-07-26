"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationPrecomputedRagSourceIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_precomputed_rag_source_identifier

EvaluationPrecomputedRagSourceIdentifiers: TypeAlias = list[
    "capo_bedrock.types.evaluation_precomputed_rag_source_identifier.EvaluationPrecomputedRagSourceIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationPrecomputedRagSourceIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationPrecomputedRagSourceIdentifiers:
    return list(data)
