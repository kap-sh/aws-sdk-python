"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankingConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

RerankingConfigurationType: TypeAlias = Literal["BEDROCK_RERANKING_MODEL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BEDROCK_RERANKING_MODEL",))


def serialize_json(value: RerankingConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> RerankingConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RerankingConfigurationType value: {data!r}"
        )
    return cast(RerankingConfigurationType, data)
