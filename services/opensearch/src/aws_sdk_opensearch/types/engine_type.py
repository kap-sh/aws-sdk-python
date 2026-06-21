"""Generated from Smithy shape ``com.amazonaws.opensearch#EngineType``."""

from typing import Literal, TypeAlias, cast

EngineType: TypeAlias = Literal[
    "OpenSearch",
    "Elasticsearch",
]


# --- restJson1 ser/de ---
def serialize_json(value: EngineType) -> str:
    return value


def deserialize_json(data: str) -> EngineType:
    return cast(EngineType, data)
