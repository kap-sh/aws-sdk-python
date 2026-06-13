"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

RerankSourceType: TypeAlias = Literal["INLINE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INLINE",))


def serialize_json(value: RerankSourceType) -> str:
    return value


def deserialize_json(data: str) -> RerankSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RerankSourceType value: {data!r}")
    return cast(RerankSourceType, data)
