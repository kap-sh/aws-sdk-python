"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StatusReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.status_reason

StatusReasons: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.status_reason.StatusReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusReasons) -> list:
    return list(value)


def deserialize_json(data: list) -> StatusReasons:
    return [item for item in data if item is not None]
