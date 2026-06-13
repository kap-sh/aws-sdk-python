"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ResponseState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

ResponseState: TypeAlias = Literal[
    "FAILURE",
    "REPROMPT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILURE",
        "REPROMPT",
    )
)


def serialize_json(value: ResponseState) -> str:
    return value


def deserialize_json(data: str) -> ResponseState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResponseState value: {data!r}")
    return cast(ResponseState, data)
