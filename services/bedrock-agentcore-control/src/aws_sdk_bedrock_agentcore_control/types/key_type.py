"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#KeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

KeyType: TypeAlias = Literal[
    "CustomerManagedKey",
    "ServiceManagedKey",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CustomerManagedKey",
        "ServiceManagedKey",
    )
)


def serialize_json(value: KeyType) -> str:
    return value


def deserialize_json(data: str) -> KeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyType value: {data!r}")
    return cast(KeyType, data)
