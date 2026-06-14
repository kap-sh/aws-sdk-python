"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserEnterprisePolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

BrowserEnterprisePolicyType: TypeAlias = Literal[
    "MANAGED",
    "RECOMMENDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANAGED",
        "RECOMMENDED",
    )
)


def serialize_json(value: BrowserEnterprisePolicyType) -> str:
    return value


def deserialize_json(data: str) -> BrowserEnterprisePolicyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BrowserEnterprisePolicyType value: {data!r}"
        )
    return cast(BrowserEnterprisePolicyType, data)
