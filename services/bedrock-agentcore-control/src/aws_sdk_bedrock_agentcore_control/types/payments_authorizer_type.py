"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentsAuthorizerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

PaymentsAuthorizerType: TypeAlias = Literal[
    "CUSTOM_JWT",
    "AWS_IAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM_JWT",
        "AWS_IAM",
    )
)


def serialize_json(value: PaymentsAuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> PaymentsAuthorizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentsAuthorizerType value: {data!r}")
    return cast(PaymentsAuthorizerType, data)
