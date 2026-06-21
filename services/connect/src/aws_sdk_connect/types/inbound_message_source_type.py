"""Generated from Smithy shape ``com.amazonaws.connect#InboundMessageSourceType``."""

from typing import Literal, TypeAlias, cast

InboundMessageSourceType: TypeAlias = Literal["RAW",]


# --- restJson1 ser/de ---
def serialize_json(value: InboundMessageSourceType) -> str:
    return value


def deserialize_json(data: str) -> InboundMessageSourceType:
    return cast(InboundMessageSourceType, data)
