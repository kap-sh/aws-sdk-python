"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#QueryTransformationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

QueryTransformationMode: TypeAlias = Literal["TEXT_TO_SQL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TEXT_TO_SQL",))


def serialize_json(value: QueryTransformationMode) -> str:
    return value


def deserialize_json(data: str) -> QueryTransformationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryTransformationMode value: {data!r}")
    return cast(QueryTransformationMode, data)
