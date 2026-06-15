"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessSkills``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_skill

HarnessSkills: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.harness_skill.HarnessSkill"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkills) -> list:
    import aws_sdk_bedrock_agentcore.types.harness_skill

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.harness_skill.serialize_json(item))
    return out


def deserialize_json(data: list) -> HarnessSkills:
    import aws_sdk_bedrock_agentcore.types.harness_skill

    out: HarnessSkills = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.harness_skill.deserialize_json(item))
    return out
