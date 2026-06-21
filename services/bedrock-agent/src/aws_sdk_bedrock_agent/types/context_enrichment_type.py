"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContextEnrichmentType``."""

from typing import Literal, TypeAlias, cast

ContextEnrichmentType: TypeAlias = Literal["BEDROCK_FOUNDATION_MODEL",]


# --- restJson1 ser/de ---
def serialize_json(value: ContextEnrichmentType) -> str:
    return value


def deserialize_json(data: str) -> ContextEnrichmentType:
    return cast(ContextEnrichmentType, data)
