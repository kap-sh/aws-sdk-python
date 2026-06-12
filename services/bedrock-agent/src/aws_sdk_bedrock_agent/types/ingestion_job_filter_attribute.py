"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

IngestionJobFilterAttribute: TypeAlias = Literal["STATUS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STATUS",))


def serialize_json(value: IngestionJobFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> IngestionJobFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngestionJobFilterAttribute value: {data!r}"
        )
    return cast(IngestionJobFilterAttribute, data)
