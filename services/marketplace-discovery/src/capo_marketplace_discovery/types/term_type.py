"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#TermType``."""

from typing import Literal, TypeAlias, cast

TermType: TypeAlias = Literal[
    "ByolPricingTerm",
    "ConfigurableUpfrontPricingTerm",
    "FixedUpfrontPricingTerm",
    "UsageBasedPricingTerm",
    "FreeTrialPricingTerm",
    "LegalTerm",
    "PaymentScheduleTerm",
    "RecurringPaymentTerm",
    "RenewalTerm",
    "SupportTerm",
    "ValidityTerm",
    "VariablePaymentTerm",
]


# --- restJson1 ser/de ---
def serialize_json(value: TermType) -> str:
    return value


def deserialize_json(data: str) -> TermType:
    return cast(TermType, data)
