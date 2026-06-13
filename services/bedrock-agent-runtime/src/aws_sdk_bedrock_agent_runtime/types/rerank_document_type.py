"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankDocumentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

RerankDocumentType: TypeAlias = Literal[
    "TEXT",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "JSON",
    )
)


def serialize_json(value: RerankDocumentType) -> str:
    return value


def deserialize_json(data: str) -> RerankDocumentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RerankDocumentType value: {data!r}")
    return cast(RerankDocumentType, data)
