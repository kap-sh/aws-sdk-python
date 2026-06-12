"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ParsingModality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ParsingModality: TypeAlias = Literal["MULTIMODAL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MULTIMODAL",))


def serialize_json(value: ParsingModality) -> str:
    return value


def deserialize_json(data: str) -> ParsingModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParsingModality value: {data!r}")
    return cast(ParsingModality, data)
