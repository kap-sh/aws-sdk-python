"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

MetadataSourceType: TypeAlias = Literal[
    "IN_LINE_ATTRIBUTE",
    "S3_LOCATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_LINE_ATTRIBUTE",
        "S3_LOCATION",
    )
)


def serialize_json(value: MetadataSourceType) -> str:
    return value


def deserialize_json(data: str) -> MetadataSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetadataSourceType value: {data!r}")
    return cast(MetadataSourceType, data)
