"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_reference

EvaluatorList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.evaluator_reference.EvaluatorReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorList) -> list:
    import capo_bedrock_agentcore_control.types.evaluator_reference

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.evaluator_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluatorList:
    import capo_bedrock_agentcore_control.types.evaluator_reference

    out: EvaluatorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.evaluator_reference.deserialize_json(
                item
            )
        )
    return out
