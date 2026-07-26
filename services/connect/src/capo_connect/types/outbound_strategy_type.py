"""Generated from Smithy shape ``com.amazonaws.connect#OutboundStrategyType``."""

from typing import Literal, TypeAlias, cast

OutboundStrategyType: TypeAlias = Literal["AGENT_FIRST",]


# --- restJson1 ser/de ---
def serialize_json(value: OutboundStrategyType) -> str:
    return value


def deserialize_json(data: str) -> OutboundStrategyType:
    return cast(OutboundStrategyType, data)
