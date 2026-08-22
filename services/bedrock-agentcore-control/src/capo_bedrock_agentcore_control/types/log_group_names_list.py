"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LogGroupNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.log_group_name

LogGroupNamesList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.log_group_name.LogGroupName"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupNamesList) -> list:
    return list(value)


def deserialize_json(data: list) -> LogGroupNamesList:
    return [item for item in data if item is not None]
