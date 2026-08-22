"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RequestHeaderAllowlist``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.header_name

RequestHeaderAllowlist: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.header_name.HeaderName"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequestHeaderAllowlist) -> list:
    return list(value)


def deserialize_json(data: list) -> RequestHeaderAllowlist:
    return [item for item in data if item is not None]
