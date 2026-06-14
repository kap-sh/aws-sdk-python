"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>Payment type enum.</p>"""
PaymentType: TypeAlias = Literal["CRYPTO_X402",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CRYPTO_X402",))


def serialize_json(value: PaymentType) -> str:
    return value


def deserialize_json(data: str) -> PaymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentType value: {data!r}")
    return cast(PaymentType, data)
