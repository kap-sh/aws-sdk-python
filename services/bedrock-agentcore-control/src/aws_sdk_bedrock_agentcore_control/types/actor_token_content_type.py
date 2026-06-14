"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ActorTokenContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ActorTokenContentType: TypeAlias = Literal[
    "NONE",
    "M2M",
    "AWS_IAM_ID_TOKEN_JWT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "M2M",
        "AWS_IAM_ID_TOKEN_JWT",
    )
)


def serialize_json(value: ActorTokenContentType) -> str:
    return value


def deserialize_json(data: str) -> ActorTokenContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActorTokenContentType value: {data!r}")
    return cast(ActorTokenContentType, data)
