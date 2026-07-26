"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankingConfigurationType``."""

from typing import Literal, TypeAlias, cast

RerankingConfigurationType: TypeAlias = Literal["BEDROCK_RERANKING_MODEL",]


# --- restJson1 ser/de ---
def serialize_json(value: RerankingConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> RerankingConfigurationType:
    return cast(RerankingConfigurationType, data)
