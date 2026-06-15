"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClaimMatchOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ClaimMatchOperatorType: TypeAlias = Literal[
    "EQUALS",
    "CONTAINS",
    "CONTAINS_ANY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "CONTAINS",
        "CONTAINS_ANY",
    )
)


def serialize_json(value: ClaimMatchOperatorType) -> str:
    return value


def deserialize_json(data: str) -> ClaimMatchOperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClaimMatchOperatorType value: {data!r}")
    return cast(ClaimMatchOperatorType, data)
