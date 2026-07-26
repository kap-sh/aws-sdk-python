"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentCredentialProviderVendorType``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported vendor types for payment providers using non-standard auth protocols.</p>"""
PaymentCredentialProviderVendorType: TypeAlias = Literal[
    "CoinbaseCDP",
    "StripePrivy",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentCredentialProviderVendorType) -> str:
    return value


def deserialize_json(data: str) -> PaymentCredentialProviderVendorType:
    return cast(PaymentCredentialProviderVendorType, data)
