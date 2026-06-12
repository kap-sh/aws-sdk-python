"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomControlMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

CustomControlMethod: TypeAlias = Literal["RETURN_CONTROL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RETURN_CONTROL",))


def serialize_json(value: CustomControlMethod) -> str:
    return value


def deserialize_json(data: str) -> CustomControlMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomControlMethod value: {data!r}")
    return cast(CustomControlMethod, data)
