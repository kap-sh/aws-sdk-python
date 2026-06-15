"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentCredentialProviderVendorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

"""<p>Supported vendor types for payment providers using non-standard auth protocols.</p>"""
PaymentCredentialProviderVendorType: TypeAlias = Literal[
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


def serialize_json(value: PaymentCredentialProviderVendorType) -> str:
    return value


def deserialize_json(data: str) -> PaymentCredentialProviderVendorType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PaymentCredentialProviderVendorType value: {data!r}"
        )
    return cast(PaymentCredentialProviderVendorType, data)
