"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InboundTokenClaimValueType``."""

from typing import Literal, TypeAlias, cast

InboundTokenClaimValueType: TypeAlias = Literal[
    "STRING",
    "STRING_ARRAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: InboundTokenClaimValueType) -> str:
    return value


def deserialize_json(data: str) -> InboundTokenClaimValueType:
    return cast(InboundTokenClaimValueType, data)
