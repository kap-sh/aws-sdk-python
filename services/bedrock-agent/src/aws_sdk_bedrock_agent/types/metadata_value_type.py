"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

MetadataValueType: TypeAlias = Literal[
    "BOOLEAN",
    "NUMBER",
    "STRING",
    "STRING_LIST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BOOLEAN",
        "NUMBER",
        "STRING",
        "STRING_LIST",
    )
)


def serialize_json(value: MetadataValueType) -> str:
    return value


def deserialize_json(data: str) -> MetadataValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetadataValueType value: {data!r}")
    return cast(MetadataValueType, data)
