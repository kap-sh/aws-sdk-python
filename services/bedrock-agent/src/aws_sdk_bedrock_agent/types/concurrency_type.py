"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConcurrencyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ConcurrencyType: TypeAlias = Literal[
    "Automatic",
    "Manual",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Automatic",
        "Manual",
    )
)


def serialize_json(value: ConcurrencyType) -> str:
    return value


def deserialize_json(data: str) -> ConcurrencyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConcurrencyType value: {data!r}")
    return cast(ConcurrencyType, data)
