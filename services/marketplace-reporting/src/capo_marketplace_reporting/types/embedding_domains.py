"""Generated from Smithy shape ``com.amazonaws.marketplacereporting#EmbeddingDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_reporting.types.embedding_domain

EmbeddingDomains: TypeAlias = list[
    "capo_marketplace_reporting.types.embedding_domain.EmbeddingDomain"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddingDomains) -> list:
    return list(value)


def deserialize_json(data: list) -> EmbeddingDomains:
    return list(data)
