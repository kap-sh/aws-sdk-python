"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContextEnrichmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ContextEnrichmentType: TypeAlias = Literal["BEDROCK_FOUNDATION_MODEL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BEDROCK_FOUNDATION_MODEL",))


def serialize_json(value: ContextEnrichmentType) -> str:
    return value


def deserialize_json(data: str) -> ContextEnrichmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContextEnrichmentType value: {data!r}")
    return cast(ContextEnrichmentType, data)
