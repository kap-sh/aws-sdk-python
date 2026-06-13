"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SatisfiedConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.satisfied_condition

SatisfiedConditions: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.satisfied_condition.SatisfiedCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: SatisfiedConditions) -> list:
    import aws_sdk_bedrock_agent_runtime.types.satisfied_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.satisfied_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SatisfiedConditions:
    import aws_sdk_bedrock_agent_runtime.types.satisfied_condition

    out: SatisfiedConditions = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.satisfied_condition.deserialize_json(
                item
            )
        )
    return out
