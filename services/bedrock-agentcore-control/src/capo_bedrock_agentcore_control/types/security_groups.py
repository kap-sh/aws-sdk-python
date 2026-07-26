"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.security_group_id

SecurityGroups: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.security_group_id.SecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroups) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroups:
    return list(data)
