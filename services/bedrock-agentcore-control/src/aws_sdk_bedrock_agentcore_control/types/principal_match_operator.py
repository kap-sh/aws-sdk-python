"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrincipalMatchOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

PrincipalMatchOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "StringEquals",
        "StringLike",
    )
)


def serialize_json(value: PrincipalMatchOperator) -> str:
    return value


def deserialize_json(data: str) -> PrincipalMatchOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrincipalMatchOperator value: {data!r}")
    return cast(PrincipalMatchOperator, data)
