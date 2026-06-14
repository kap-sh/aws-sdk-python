"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchValueStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.match_value_string

MatchValueStringList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.match_value_string.MatchValueString"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchValueStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> MatchValueStringList:
    return list(data)
