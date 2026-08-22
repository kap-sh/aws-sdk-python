"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSkills``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_skill

HarnessSkills: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.harness_skill.HarnessSkill"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkills) -> list:
    import capo_bedrock_agentcore_control.types.harness_skill

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.harness_skill.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessSkills:
    import capo_bedrock_agentcore_control.types.harness_skill

    out: HarnessSkills = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.harness_skill.deserialize_json(item)
        )
    return out
