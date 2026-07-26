"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankingMetadataSelectionMode``."""

from typing import Literal, TypeAlias, cast

RerankingMetadataSelectionMode: TypeAlias = Literal[
    "SELECTIVE",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RerankingMetadataSelectionMode) -> str:
    return value


def deserialize_json(data: str) -> RerankingMetadataSelectionMode:
    return cast(RerankingMetadataSelectionMode, data)
