"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EnrichmentStrategyMethod``."""

from typing import Literal, TypeAlias, cast

EnrichmentStrategyMethod: TypeAlias = Literal["CHUNK_ENTITY_EXTRACTION",]


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentStrategyMethod) -> str:
    return value


def deserialize_json(data: str) -> EnrichmentStrategyMethod:
    return cast(EnrichmentStrategyMethod, data)
