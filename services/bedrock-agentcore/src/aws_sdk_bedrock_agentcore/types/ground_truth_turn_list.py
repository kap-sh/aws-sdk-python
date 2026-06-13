"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthTurnList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.ground_truth_turn

GroundTruthTurnList: TypeAlias = list["aws_sdk_bedrock_agentcore.types.ground_truth_turn.GroundTruthTurn"]


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthTurnList) -> list:
    import aws_sdk_bedrock_agentcore.types.ground_truth_turn
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.ground_truth_turn.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroundTruthTurnList:
    import aws_sdk_bedrock_agentcore.types.ground_truth_turn
    out: GroundTruthTurnList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.ground_truth_turn.deserialize_json(item))
    return out