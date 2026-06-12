"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EnrichmentStrategyMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

EnrichmentStrategyMethod: TypeAlias = Literal["CHUNK_ENTITY_EXTRACTION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CHUNK_ENTITY_EXTRACTION",))


def serialize_json(value: EnrichmentStrategyMethod) -> str:
    return value


def deserialize_json(data: str) -> EnrichmentStrategyMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnrichmentStrategyMethod value: {data!r}")
    return cast(EnrichmentStrategyMethod, data)
