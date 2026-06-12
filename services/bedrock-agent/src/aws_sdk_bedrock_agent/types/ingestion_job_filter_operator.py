"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

IngestionJobFilterOperator: TypeAlias = Literal["EQ",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQ",))


def serialize_json(value: IngestionJobFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> IngestionJobFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngestionJobFilterOperator value: {data!r}"
        )
    return cast(IngestionJobFilterOperator, data)
