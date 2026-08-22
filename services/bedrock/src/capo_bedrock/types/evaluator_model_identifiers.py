"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluatorModelIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.evaluator_model_identifier

EvaluatorModelIdentifiers: TypeAlias = list[
    "capo_bedrock.types.evaluator_model_identifier.EvaluatorModelIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorModelIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluatorModelIdentifiers:
    return [item for item in data if item is not None]
