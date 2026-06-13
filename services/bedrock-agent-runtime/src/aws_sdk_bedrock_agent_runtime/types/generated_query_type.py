"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GeneratedQueryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GeneratedQueryType: TypeAlias = Literal["REDSHIFT_SQL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("REDSHIFT_SQL",))


def serialize_json(value: GeneratedQueryType) -> str:
    return value


def deserialize_json(data: str) -> GeneratedQueryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeneratedQueryType value: {data!r}")
    return cast(GeneratedQueryType, data)
