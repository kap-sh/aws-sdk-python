"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#VectorSearchRerankingConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

VectorSearchRerankingConfigurationType: TypeAlias = Literal["BEDROCK_RERANKING_MODEL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BEDROCK_RERANKING_MODEL",))


def serialize_json(value: VectorSearchRerankingConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> VectorSearchRerankingConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VectorSearchRerankingConfigurationType value: {data!r}"
        )
    return cast(VectorSearchRerankingConfigurationType, data)
