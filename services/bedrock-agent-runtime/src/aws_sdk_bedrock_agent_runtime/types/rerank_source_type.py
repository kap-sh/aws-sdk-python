"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankSourceType``."""

from typing import Literal, TypeAlias, cast

RerankSourceType: TypeAlias = Literal["INLINE",]


# --- restJson1 ser/de ---
def serialize_json(value: RerankSourceType) -> str:
    return value


def deserialize_json(data: str) -> RerankSourceType:
    return cast(RerankSourceType, data)
