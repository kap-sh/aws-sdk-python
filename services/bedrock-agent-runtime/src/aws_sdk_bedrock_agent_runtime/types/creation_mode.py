"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CreationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

CreationMode: TypeAlias = Literal[
    "DEFAULT",
    "OVERRIDDEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "OVERRIDDEN",
    )
)


def serialize_json(value: CreationMode) -> str:
    return value


def deserialize_json(data: str) -> CreationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CreationMode value: {data!r}")
    return cast(CreationMode, data)
