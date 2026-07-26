"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AliasInvocationState``."""

from typing import Literal, TypeAlias, cast

"""Enum representing the invocation state of an agent alias"""
AliasInvocationState: TypeAlias = Literal[
    "ACCEPT_INVOCATIONS",
    "REJECT_INVOCATIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AliasInvocationState) -> str:
    return value


def deserialize_json(data: str) -> AliasInvocationState:
    return cast(AliasInvocationState, data)
