"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConfluenceHostType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ConfluenceHostType: TypeAlias = Literal["SAAS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SAAS",))


def serialize_json(value: ConfluenceHostType) -> str:
    return value


def deserialize_json(data: str) -> ConfluenceHostType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfluenceHostType value: {data!r}")
    return cast(ConfluenceHostType, data)
