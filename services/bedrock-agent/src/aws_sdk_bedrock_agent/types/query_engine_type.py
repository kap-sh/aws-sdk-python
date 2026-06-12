"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryEngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

QueryEngineType: TypeAlias = Literal["REDSHIFT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("REDSHIFT",))


def serialize_json(value: QueryEngineType) -> str:
    return value


def deserialize_json(data: str) -> QueryEngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryEngineType value: {data!r}")
    return cast(QueryEngineType, data)
