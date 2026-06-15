"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InboundTokenClaimValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

InboundTokenClaimValueType: TypeAlias = Literal[
    "STRING",
    "STRING_ARRAY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "STRING_ARRAY",
    )
)


def serialize_json(value: InboundTokenClaimValueType) -> str:
    return value


def deserialize_json(data: str) -> InboundTokenClaimValueType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InboundTokenClaimValueType value: {data!r}"
        )
    return cast(InboundTokenClaimValueType, data)
