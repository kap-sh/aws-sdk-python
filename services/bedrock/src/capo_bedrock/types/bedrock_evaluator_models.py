"""Generated from Smithy shape ``com.amazonaws.bedrock#BedrockEvaluatorModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_evaluator_model

BedrockEvaluatorModels: TypeAlias = list[
    "capo_bedrock.types.bedrock_evaluator_model.BedrockEvaluatorModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: BedrockEvaluatorModels) -> list:
    import capo_bedrock.types.bedrock_evaluator_model

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.bedrock_evaluator_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> BedrockEvaluatorModels:
    import capo_bedrock.types.bedrock_evaluator_model

    out: BedrockEvaluatorModels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.bedrock_evaluator_model.deserialize_json(item))
    return out
