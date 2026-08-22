"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_id


class _EvaluatorReference_evaluatorId(TypedDict, closed=True):
    evaluatorId: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"


EvaluatorReference: TypeAlias = _EvaluatorReference_evaluatorId


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorReference) -> dict:
    if "evaluatorId" in value:
        return {"evaluatorId": value["evaluatorId"]}
    else:
        raise SerializationError("EvaluatorReference: no variant present")


def deserialize_json(data: dict) -> EvaluatorReference:
    if data.get("evaluatorId") is not None:
        return {"evaluatorId": data["evaluatorId"]}
    else:
        raise DeserializationError("EvaluatorReference: no recognized variant key")
