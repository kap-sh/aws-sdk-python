"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EmbeddingDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

"""<p>Bedrock models embedding data type. Can be either float32 or binary.</p>"""
EmbeddingDataType: TypeAlias = Literal[
    "FLOAT32",
    "BINARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLOAT32",
        "BINARY",
    )
)


def serialize_json(value: EmbeddingDataType) -> str:
    return value


def deserialize_json(data: str) -> EmbeddingDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmbeddingDataType value: {data!r}")
    return cast(EmbeddingDataType, data)
