"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationPrecomputedRetrieveSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_precomputed_rag_source_identifier


class EvaluationPrecomputedRetrieveSourceConfig(TypedDict, closed=True):
    rag_source_identifier: "capo_bedrock.types.evaluation_precomputed_rag_source_identifier.EvaluationPrecomputedRagSourceIdentifier"
    """<p>A label that identifies the RAG source used for a retrieve-only Knowledge Base evaluation job where you provide your own inference response data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationPrecomputedRetrieveSourceConfig) -> dict:
    out: dict = {}
    out["ragSourceIdentifier"] = value["rag_source_identifier"]
    return out


def deserialize_json(data: dict) -> EvaluationPrecomputedRetrieveSourceConfig:
    out: EvaluationPrecomputedRetrieveSourceConfig = {}  # type: ignore[typeddict-item]
    if "ragSourceIdentifier" in data:
        out["rag_source_identifier"] = data["ragSourceIdentifier"]
    else:
        raise DeserializationError(
            "EvaluationPrecomputedRetrieveSourceConfig.rag_source_identifier required"
        )
    return out
