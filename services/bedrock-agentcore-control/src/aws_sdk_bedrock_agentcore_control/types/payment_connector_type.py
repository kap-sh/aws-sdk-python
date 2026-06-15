"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentConnectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

PaymentConnectorType: TypeAlias = Literal[
    "CoinbaseCDP",
    "StripePrivy",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CoinbaseCDP",
        "StripePrivy",
    )
)


def serialize_json(value: PaymentConnectorType) -> str:
    return value


def deserialize_json(data: str) -> PaymentConnectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentConnectorType value: {data!r}")
    return cast(PaymentConnectorType, data)
