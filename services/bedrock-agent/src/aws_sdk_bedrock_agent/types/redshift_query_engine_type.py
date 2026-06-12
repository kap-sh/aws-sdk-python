"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

RedshiftQueryEngineType: TypeAlias = Literal[
    "SERVERLESS",
    "PROVISIONED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVERLESS",
        "PROVISIONED",
    )
)


def serialize_json(value: RedshiftQueryEngineType) -> str:
    return value


def deserialize_json(data: str) -> RedshiftQueryEngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RedshiftQueryEngineType value: {data!r}")
    return cast(RedshiftQueryEngineType, data)
