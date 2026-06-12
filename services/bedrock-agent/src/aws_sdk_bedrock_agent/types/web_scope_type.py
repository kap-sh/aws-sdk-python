"""Generated from Smithy shape ``com.amazonaws.bedrockagent#WebScopeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

WebScopeType: TypeAlias = Literal[
    "HOST_ONLY",
    "SUBDOMAINS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOST_ONLY",
        "SUBDOMAINS",
    )
)


def serialize_json(value: WebScopeType) -> str:
    return value


def deserialize_json(data: str) -> WebScopeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WebScopeType value: {data!r}")
    return cast(WebScopeType, data)
