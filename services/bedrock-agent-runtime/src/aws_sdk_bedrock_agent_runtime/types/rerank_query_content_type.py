"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankQueryContentType``."""

from typing import Literal, TypeAlias, cast

RerankQueryContentType: TypeAlias = Literal["TEXT",]


# --- restJson1 ser/de ---
def serialize_json(value: RerankQueryContentType) -> str:
    return value


def deserialize_json(data: str) -> RerankQueryContentType:
    return cast(RerankQueryContentType, data)
