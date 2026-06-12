"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConfluenceAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ConfluenceAuthType: TypeAlias = Literal[
    "BASIC",
    "OAUTH2_CLIENT_CREDENTIALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "OAUTH2_CLIENT_CREDENTIALS",
    )
)


def serialize_json(value: ConfluenceAuthType) -> str:
    return value


def deserialize_json(data: str) -> ConfluenceAuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfluenceAuthType value: {data!r}")
    return cast(ConfluenceAuthType, data)
