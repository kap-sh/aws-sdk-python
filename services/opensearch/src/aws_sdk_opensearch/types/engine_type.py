"""Generated from Smithy shape ``com.amazonaws.opensearch#EngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

EngineType: TypeAlias = Literal[
    "OpenSearch",
    "Elasticsearch",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OpenSearch",
        "Elasticsearch",
    )
)


def serialize_json(value: EngineType) -> str:
    return value


def deserialize_json(data: str) -> EngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngineType value: {data!r}")
    return cast(EngineType, data)
