"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MetadataValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

MetadataValueType: TypeAlias = Literal[
    "STRING",
    "STRINGLIST",
    "NUMBER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "STRINGLIST",
        "NUMBER",
    )
)


def serialize_json(value: MetadataValueType) -> str:
    return value


def deserialize_json(data: str) -> MetadataValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetadataValueType value: {data!r}")
    return cast(MetadataValueType, data)
