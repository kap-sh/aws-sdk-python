"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContentDataSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ContentDataSourceType: TypeAlias = Literal[
    "CUSTOM",
    "S3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM",
        "S3",
    )
)


def serialize_json(value: ContentDataSourceType) -> str:
    return value


def deserialize_json(data: str) -> ContentDataSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentDataSourceType value: {data!r}")
    return cast(ContentDataSourceType, data)
