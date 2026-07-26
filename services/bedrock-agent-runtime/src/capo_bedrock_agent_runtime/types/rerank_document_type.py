"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankDocumentType``."""

from typing import Literal, TypeAlias, cast

RerankDocumentType: TypeAlias = Literal[
    "TEXT",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: RerankDocumentType) -> str:
    return value


def deserialize_json(data: str) -> RerankDocumentType:
    return cast(RerankDocumentType, data)
