"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationBedrockModelIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_bedrock_model_identifier

EvaluationBedrockModelIdentifiers: TypeAlias = list[
    "capo_bedrock.types.evaluation_bedrock_model_identifier.EvaluationBedrockModelIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationBedrockModelIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationBedrockModelIdentifiers:
    return [item for item in data if item is not None]
