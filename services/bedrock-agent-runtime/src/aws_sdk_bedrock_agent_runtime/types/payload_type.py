"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PayloadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

PayloadType: TypeAlias = Literal[
    "TEXT",
    "RETURN_CONTROL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "RETURN_CONTROL",
    )
)


def serialize_json(value: PayloadType) -> str:
    return value


def deserialize_json(data: str) -> PayloadType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PayloadType value: {data!r}")
    return cast(PayloadType, data)
