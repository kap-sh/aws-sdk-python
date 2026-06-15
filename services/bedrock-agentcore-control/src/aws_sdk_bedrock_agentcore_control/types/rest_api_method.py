"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RestApiMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

RestApiMethod: TypeAlias = Literal[
    "GET",
    "DELETE",
    "HEAD",
    "OPTIONS",
    "PATCH",
    "PUT",
    "POST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GET",
        "DELETE",
        "HEAD",
        "OPTIONS",
        "PATCH",
        "PUT",
        "POST",
    )
)


def serialize_json(value: RestApiMethod) -> str:
    return value


def deserialize_json(data: str) -> RestApiMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RestApiMethod value: {data!r}")
    return cast(RestApiMethod, data)
