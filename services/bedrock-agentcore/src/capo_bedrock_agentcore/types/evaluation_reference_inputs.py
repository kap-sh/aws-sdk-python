"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationReferenceInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_reference_input

EvaluationReferenceInputs: TypeAlias = list[
    "capo_bedrock_agentcore.types.evaluation_reference_input.EvaluationReferenceInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReferenceInputs) -> list:
    import capo_bedrock_agentcore.types.evaluation_reference_input

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.evaluation_reference_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationReferenceInputs:
    import capo_bedrock_agentcore.types.evaluation_reference_input

    out: EvaluationReferenceInputs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.evaluation_reference_input.deserialize_json(
                item
            )
        )
    return out
