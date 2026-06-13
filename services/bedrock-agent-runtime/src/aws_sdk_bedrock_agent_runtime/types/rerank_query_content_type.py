"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankQueryContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

RerankQueryContentType: TypeAlias = Literal["TEXT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TEXT",))


def serialize_json(value: RerankQueryContentType) -> str:
    return value


def deserialize_json(data: str) -> RerankQueryContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RerankQueryContentType value: {data!r}")
    return cast(RerankQueryContentType, data)
