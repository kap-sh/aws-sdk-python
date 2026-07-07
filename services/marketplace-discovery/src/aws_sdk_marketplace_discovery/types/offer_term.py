"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferTerm``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.byol_pricing_term
    import aws_sdk_marketplace_discovery.types.configurable_upfront_pricing_term
    import aws_sdk_marketplace_discovery.types.fixed_upfront_pricing_term
    import aws_sdk_marketplace_discovery.types.free_trial_pricing_term
    import aws_sdk_marketplace_discovery.types.legal_term
    import aws_sdk_marketplace_discovery.types.payment_schedule_term
    import aws_sdk_marketplace_discovery.types.recurring_payment_term
    import aws_sdk_marketplace_discovery.types.renewal_term
    import aws_sdk_marketplace_discovery.types.support_term
    import aws_sdk_marketplace_discovery.types.usage_based_pricing_term
    import aws_sdk_marketplace_discovery.types.validity_term
    import aws_sdk_marketplace_discovery.types.variable_payment_term


class _OfferTerm_byolPricingTerm(TypedDict, closed=True):
    byolPricingTerm: (
        "aws_sdk_marketplace_discovery.types.byol_pricing_term.ByolPricingTerm"
    )


class _OfferTerm_configurableUpfrontPricingTerm(TypedDict, closed=True):
    configurableUpfrontPricingTerm: "aws_sdk_marketplace_discovery.types.configurable_upfront_pricing_term.ConfigurableUpfrontPricingTerm"


class _OfferTerm_fixedUpfrontPricingTerm(TypedDict, closed=True):
    fixedUpfrontPricingTerm: "aws_sdk_marketplace_discovery.types.fixed_upfront_pricing_term.FixedUpfrontPricingTerm"


class _OfferTerm_freeTrialPricingTerm(TypedDict, closed=True):
    freeTrialPricingTerm: "aws_sdk_marketplace_discovery.types.free_trial_pricing_term.FreeTrialPricingTerm"


class _OfferTerm_legalTerm(TypedDict, closed=True):
    legalTerm: "aws_sdk_marketplace_discovery.types.legal_term.LegalTerm"


class _OfferTerm_paymentScheduleTerm(TypedDict, closed=True):
    paymentScheduleTerm: (
        "aws_sdk_marketplace_discovery.types.payment_schedule_term.PaymentScheduleTerm"
    )


class _OfferTerm_recurringPaymentTerm(TypedDict, closed=True):
    recurringPaymentTerm: "aws_sdk_marketplace_discovery.types.recurring_payment_term.RecurringPaymentTerm"


class _OfferTerm_renewalTerm(TypedDict, closed=True):
    renewalTerm: "aws_sdk_marketplace_discovery.types.renewal_term.RenewalTerm"


class _OfferTerm_supportTerm(TypedDict, closed=True):
    supportTerm: "aws_sdk_marketplace_discovery.types.support_term.SupportTerm"


class _OfferTerm_usageBasedPricingTerm(TypedDict, closed=True):
    usageBasedPricingTerm: "aws_sdk_marketplace_discovery.types.usage_based_pricing_term.UsageBasedPricingTerm"


class _OfferTerm_validityTerm(TypedDict, closed=True):
    validityTerm: "aws_sdk_marketplace_discovery.types.validity_term.ValidityTerm"


class _OfferTerm_variablePaymentTerm(TypedDict, closed=True):
    variablePaymentTerm: (
        "aws_sdk_marketplace_discovery.types.variable_payment_term.VariablePaymentTerm"
    )


OfferTerm: TypeAlias = (
    _OfferTerm_byolPricingTerm
    | _OfferTerm_configurableUpfrontPricingTerm
    | _OfferTerm_fixedUpfrontPricingTerm
    | _OfferTerm_freeTrialPricingTerm
    | _OfferTerm_legalTerm
    | _OfferTerm_paymentScheduleTerm
    | _OfferTerm_recurringPaymentTerm
    | _OfferTerm_renewalTerm
    | _OfferTerm_supportTerm
    | _OfferTerm_usageBasedPricingTerm
    | _OfferTerm_validityTerm
    | _OfferTerm_variablePaymentTerm
)


# --- restJson1 ser/de ---
def serialize_json(value: OfferTerm) -> dict:
    if "byolPricingTerm" in value:
        import aws_sdk_marketplace_discovery.types.byol_pricing_term

        return {
            "byolPricingTerm": aws_sdk_marketplace_discovery.types.byol_pricing_term.serialize_json(
                value["byolPricingTerm"]
            )
        }
    elif "configurableUpfrontPricingTerm" in value:
        import aws_sdk_marketplace_discovery.types.configurable_upfront_pricing_term

        return {
            "configurableUpfrontPricingTerm": aws_sdk_marketplace_discovery.types.configurable_upfront_pricing_term.serialize_json(
                value["configurableUpfrontPricingTerm"]
            )
        }
    elif "fixedUpfrontPricingTerm" in value:
        import aws_sdk_marketplace_discovery.types.fixed_upfront_pricing_term

        return {
            "fixedUpfrontPricingTerm": aws_sdk_marketplace_discovery.types.fixed_upfront_pricing_term.serialize_json(
                value["fixedUpfrontPricingTerm"]
            )
        }
    elif "freeTrialPricingTerm" in value:
        import aws_sdk_marketplace_discovery.types.free_trial_pricing_term

        return {
            "freeTrialPricingTerm": aws_sdk_marketplace_discovery.types.free_trial_pricing_term.serialize_json(
                value["freeTrialPricingTerm"]
            )
        }
    elif "legalTerm" in value:
        import aws_sdk_marketplace_discovery.types.legal_term

        return {
            "legalTerm": aws_sdk_marketplace_discovery.types.legal_term.serialize_json(
                value["legalTerm"]
            )
        }
    elif "paymentScheduleTerm" in value:
        import aws_sdk_marketplace_discovery.types.payment_schedule_term

        return {
            "paymentScheduleTerm": aws_sdk_marketplace_discovery.types.payment_schedule_term.serialize_json(
                value["paymentScheduleTerm"]
            )
        }
    elif "recurringPaymentTerm" in value:
        import aws_sdk_marketplace_discovery.types.recurring_payment_term

        return {
            "recurringPaymentTerm": aws_sdk_marketplace_discovery.types.recurring_payment_term.serialize_json(
                value["recurringPaymentTerm"]
            )
        }
    elif "renewalTerm" in value:
        import aws_sdk_marketplace_discovery.types.renewal_term

        return {
            "renewalTerm": aws_sdk_marketplace_discovery.types.renewal_term.serialize_json(
                value["renewalTerm"]
            )
        }
    elif "supportTerm" in value:
        import aws_sdk_marketplace_discovery.types.support_term

        return {
            "supportTerm": aws_sdk_marketplace_discovery.types.support_term.serialize_json(
                value["supportTerm"]
            )
        }
    elif "usageBasedPricingTerm" in value:
        import aws_sdk_marketplace_discovery.types.usage_based_pricing_term

        return {
            "usageBasedPricingTerm": aws_sdk_marketplace_discovery.types.usage_based_pricing_term.serialize_json(
                value["usageBasedPricingTerm"]
            )
        }
    elif "validityTerm" in value:
        import aws_sdk_marketplace_discovery.types.validity_term

        return {
            "validityTerm": aws_sdk_marketplace_discovery.types.validity_term.serialize_json(
                value["validityTerm"]
            )
        }
    elif "variablePaymentTerm" in value:
        import aws_sdk_marketplace_discovery.types.variable_payment_term

        return {
            "variablePaymentTerm": aws_sdk_marketplace_discovery.types.variable_payment_term.serialize_json(
                value["variablePaymentTerm"]
            )
        }
    else:
        raise SerializationError("OfferTerm: no variant present")


def deserialize_json(data: dict) -> OfferTerm:
    if "byolPricingTerm" in data:
        import aws_sdk_marketplace_discovery.types.byol_pricing_term

        return {
            "byolPricingTerm": aws_sdk_marketplace_discovery.types.byol_pricing_term.deserialize_json(
                data["byolPricingTerm"]
            )
        }
    elif "configurableUpfrontPricingTerm" in data:
        import aws_sdk_marketplace_discovery.types.configurable_upfront_pricing_term

        return {
            "configurableUpfrontPricingTerm": aws_sdk_marketplace_discovery.types.configurable_upfront_pricing_term.deserialize_json(
                data["configurableUpfrontPricingTerm"]
            )
        }
    elif "fixedUpfrontPricingTerm" in data:
        import aws_sdk_marketplace_discovery.types.fixed_upfront_pricing_term

        return {
            "fixedUpfrontPricingTerm": aws_sdk_marketplace_discovery.types.fixed_upfront_pricing_term.deserialize_json(
                data["fixedUpfrontPricingTerm"]
            )
        }
    elif "freeTrialPricingTerm" in data:
        import aws_sdk_marketplace_discovery.types.free_trial_pricing_term

        return {
            "freeTrialPricingTerm": aws_sdk_marketplace_discovery.types.free_trial_pricing_term.deserialize_json(
                data["freeTrialPricingTerm"]
            )
        }
    elif "legalTerm" in data:
        import aws_sdk_marketplace_discovery.types.legal_term

        return {
            "legalTerm": aws_sdk_marketplace_discovery.types.legal_term.deserialize_json(
                data["legalTerm"]
            )
        }
    elif "paymentScheduleTerm" in data:
        import aws_sdk_marketplace_discovery.types.payment_schedule_term

        return {
            "paymentScheduleTerm": aws_sdk_marketplace_discovery.types.payment_schedule_term.deserialize_json(
                data["paymentScheduleTerm"]
            )
        }
    elif "recurringPaymentTerm" in data:
        import aws_sdk_marketplace_discovery.types.recurring_payment_term

        return {
            "recurringPaymentTerm": aws_sdk_marketplace_discovery.types.recurring_payment_term.deserialize_json(
                data["recurringPaymentTerm"]
            )
        }
    elif "renewalTerm" in data:
        import aws_sdk_marketplace_discovery.types.renewal_term

        return {
            "renewalTerm": aws_sdk_marketplace_discovery.types.renewal_term.deserialize_json(
                data["renewalTerm"]
            )
        }
    elif "supportTerm" in data:
        import aws_sdk_marketplace_discovery.types.support_term

        return {
            "supportTerm": aws_sdk_marketplace_discovery.types.support_term.deserialize_json(
                data["supportTerm"]
            )
        }
    elif "usageBasedPricingTerm" in data:
        import aws_sdk_marketplace_discovery.types.usage_based_pricing_term

        return {
            "usageBasedPricingTerm": aws_sdk_marketplace_discovery.types.usage_based_pricing_term.deserialize_json(
                data["usageBasedPricingTerm"]
            )
        }
    elif "validityTerm" in data:
        import aws_sdk_marketplace_discovery.types.validity_term

        return {
            "validityTerm": aws_sdk_marketplace_discovery.types.validity_term.deserialize_json(
                data["validityTerm"]
            )
        }
    elif "variablePaymentTerm" in data:
        import aws_sdk_marketplace_discovery.types.variable_payment_term

        return {
            "variablePaymentTerm": aws_sdk_marketplace_discovery.types.variable_payment_term.deserialize_json(
                data["variablePaymentTerm"]
            )
        }
    else:
        raise DeserializationError("OfferTerm: no recognized variant key")
