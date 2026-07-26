"""Generated from Smithy shape ``com.amazonaws.bedrock#VectorSearchRerankingConfigurationType``."""

from typing import Literal, TypeAlias, cast

VectorSearchRerankingConfigurationType: TypeAlias = Literal["BEDROCK_RERANKING_MODEL",]


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchRerankingConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> VectorSearchRerankingConfigurationType:
    return cast(VectorSearchRerankingConfigurationType, data)
