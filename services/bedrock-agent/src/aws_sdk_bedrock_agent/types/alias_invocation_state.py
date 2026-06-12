"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AliasInvocationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

"""Enum representing the invocation state of an agent alias"""
AliasInvocationState: TypeAlias = Literal[
    "ACCEPT_INVOCATIONS",
    "REJECT_INVOCATIONS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCEPT_INVOCATIONS",
        "REJECT_INVOCATIONS",
    )
)


def serialize_json(value: AliasInvocationState) -> str:
    return value


def deserialize_json(data: str) -> AliasInvocationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AliasInvocationState value: {data!r}")
    return cast(AliasInvocationState, data)
