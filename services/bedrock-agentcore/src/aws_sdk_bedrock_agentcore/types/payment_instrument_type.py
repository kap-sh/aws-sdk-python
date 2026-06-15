"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrumentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The type of payment instrument.</p>"""
PaymentInstrumentType: TypeAlias = Literal["EMBEDDED_CRYPTO_WALLET",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EMBEDDED_CRYPTO_WALLET",))


def serialize_json(value: PaymentInstrumentType) -> str:
    return value


def deserialize_json(data: str) -> PaymentInstrumentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentInstrumentType value: {data!r}")
    return cast(PaymentInstrumentType, data)
