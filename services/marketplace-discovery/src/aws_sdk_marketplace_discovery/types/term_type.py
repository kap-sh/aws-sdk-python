"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#TermType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: TermType) -> str:
    return value


def deserialize_json(data: str) -> TermType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TermType value: {data!r}")
    return cast(TermType, data)
