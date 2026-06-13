"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CachePointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

CachePointType: TypeAlias = Literal["default",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("default",))


def serialize_json(value: CachePointType) -> str:
    return value


def deserialize_json(data: str) -> CachePointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CachePointType value: {data!r}")
    return cast(CachePointType, data)
