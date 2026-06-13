"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerAuthorizationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Supported authorization methods for MCP servers.</p>"""
MCPServerAuthorizationMethod: TypeAlias = Literal[
    "oauth-client-credentials",
    "oauth-3lo",
    "api-key",
    "bearer-token",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "oauth-client-credentials",
        "oauth-3lo",
        "api-key",
        "bearer-token",
    )
)


def serialize_json(value: MCPServerAuthorizationMethod) -> str:
    return value


def deserialize_json(data: str) -> MCPServerAuthorizationMethod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MCPServerAuthorizationMethod value: {data!r}"
        )
    return cast(MCPServerAuthorizationMethod, data)
