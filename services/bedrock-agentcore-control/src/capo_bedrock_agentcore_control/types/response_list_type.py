"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResponseListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.response_type

ResponseListType: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.response_type.ResponseType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseListType) -> list:
    return list(value)


def deserialize_json(data: list) -> ResponseListType:
    return list(data)
