"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.evaluator_reference

EvaluatorList: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.evaluator_reference.EvaluatorReference"]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.evaluator_reference
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.evaluator_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluatorList:
    import aws_sdk_bedrock_agentcore_control.types.evaluator_reference
    out: EvaluatorList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.evaluator_reference.deserialize_json(item))
    return out