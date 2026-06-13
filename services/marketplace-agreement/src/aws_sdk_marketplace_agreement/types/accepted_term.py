"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptedTerm``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_marketplace_agreement.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.byol_pricing_term
    import aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term
    import aws_sdk_marketplace_agreement.types.fixed_upfront_pricing_term
    import aws_sdk_marketplace_agreement.types.free_trial_pricing_term
    import aws_sdk_marketplace_agreement.types.legal_term
    import aws_sdk_marketplace_agreement.types.payment_schedule_term
    import aws_sdk_marketplace_agreement.types.recurring_payment_term
    import aws_sdk_marketplace_agreement.types.renewal_term
    import aws_sdk_marketplace_agreement.types.support_term
    import aws_sdk_marketplace_agreement.types.usage_based_pricing_term
    import aws_sdk_marketplace_agreement.types.validity_term
    import aws_sdk_marketplace_agreement.types.variable_payment_term


class _AcceptedTerm_legalTerm(TypedDict):
    legalTerm: "aws_sdk_marketplace_agreement.types.legal_term.LegalTerm"


class _AcceptedTerm_supportTerm(TypedDict):
    supportTerm: "aws_sdk_marketplace_agreement.types.support_term.SupportTerm"


class _AcceptedTerm_renewalTerm(TypedDict):
    renewalTerm: "aws_sdk_marketplace_agreement.types.renewal_term.RenewalTerm"


class _AcceptedTerm_usageBasedPricingTerm(TypedDict):
    usageBasedPricingTerm: "aws_sdk_marketplace_agreement.types.usage_based_pricing_term.UsageBasedPricingTerm"


class _AcceptedTerm_configurableUpfrontPricingTerm(TypedDict):
    configurableUpfrontPricingTerm: "aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term.ConfigurableUpfrontPricingTerm"


class _AcceptedTerm_byolPricingTerm(TypedDict):
    byolPricingTerm: (
        "aws_sdk_marketplace_agreement.types.byol_pricing_term.ByolPricingTerm"
    )


class _AcceptedTerm_recurringPaymentTerm(TypedDict):
    recurringPaymentTerm: "aws_sdk_marketplace_agreement.types.recurring_payment_term.RecurringPaymentTerm"


class _AcceptedTerm_validityTerm(TypedDict):
    validityTerm: "aws_sdk_marketplace_agreement.types.validity_term.ValidityTerm"


class _AcceptedTerm_paymentScheduleTerm(TypedDict):
    paymentScheduleTerm: (
        "aws_sdk_marketplace_agreement.types.payment_schedule_term.PaymentScheduleTerm"
    )


class _AcceptedTerm_freeTrialPricingTerm(TypedDict):
    freeTrialPricingTerm: "aws_sdk_marketplace_agreement.types.free_trial_pricing_term.FreeTrialPricingTerm"


class _AcceptedTerm_fixedUpfrontPricingTerm(TypedDict):
    fixedUpfrontPricingTerm: "aws_sdk_marketplace_agreement.types.fixed_upfront_pricing_term.FixedUpfrontPricingTerm"


class _AcceptedTerm_variablePaymentTerm(TypedDict):
    variablePaymentTerm: (
        "aws_sdk_marketplace_agreement.types.variable_payment_term.VariablePaymentTerm"
    )


AcceptedTerm: TypeAlias = (
    _AcceptedTerm_legalTerm
    | _AcceptedTerm_supportTerm
    | _AcceptedTerm_renewalTerm
    | _AcceptedTerm_usageBasedPricingTerm
    | _AcceptedTerm_configurableUpfrontPricingTerm
    | _AcceptedTerm_byolPricingTerm
    | _AcceptedTerm_recurringPaymentTerm
    | _AcceptedTerm_validityTerm
    | _AcceptedTerm_paymentScheduleTerm
    | _AcceptedTerm_freeTrialPricingTerm
    | _AcceptedTerm_fixedUpfrontPricingTerm
    | _AcceptedTerm_variablePaymentTerm
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptedTerm) -> dict:
    if "legalTerm" in value:
        import aws_sdk_marketplace_agreement.types.legal_term

        return {
            "legalTerm": aws_sdk_marketplace_agreement.types.legal_term.serialize_aws_json_1_0(
                value["legalTerm"]
            )
        }
    elif "supportTerm" in value:
        import aws_sdk_marketplace_agreement.types.support_term

        return {
            "supportTerm": aws_sdk_marketplace_agreement.types.support_term.serialize_aws_json_1_0(
                value["supportTerm"]
            )
        }
    elif "renewalTerm" in value:
        import aws_sdk_marketplace_agreement.types.renewal_term

        return {
            "renewalTerm": aws_sdk_marketplace_agreement.types.renewal_term.serialize_aws_json_1_0(
                value["renewalTerm"]
            )
        }
    elif "usageBasedPricingTerm" in value:
        import aws_sdk_marketplace_agreement.types.usage_based_pricing_term

        return {
            "usageBasedPricingTerm": aws_sdk_marketplace_agreement.types.usage_based_pricing_term.serialize_aws_json_1_0(
                value["usageBasedPricingTerm"]
            )
        }
    elif "configurableUpfrontPricingTerm" in value:
        import aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term

        return {
            "configurableUpfrontPricingTerm": aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term.serialize_aws_json_1_0(
                value["configurableUpfrontPricingTerm"]
            )
        }
    elif "byolPricingTerm" in value:
        import aws_sdk_marketplace_agreement.types.byol_pricing_term

        return {
            "byolPricingTerm": aws_sdk_marketplace_agreement.types.byol_pricing_term.serialize_aws_json_1_0(
                value["byolPricingTerm"]
            )
        }
    elif "recurringPaymentTerm" in value:
        import aws_sdk_marketplace_agreement.types.recurring_payment_term

        return {
            "recurringPaymentTerm": aws_sdk_marketplace_agreement.types.recurring_payment_term.serialize_aws_json_1_0(
                value["recurringPaymentTerm"]
            )
        }
    elif "validityTerm" in value:
        import aws_sdk_marketplace_agreement.types.validity_term

        return {
            "validityTerm": aws_sdk_marketplace_agreement.types.validity_term.serialize_aws_json_1_0(
                value["validityTerm"]
            )
        }
    elif "paymentScheduleTerm" in value:
        import aws_sdk_marketplace_agreement.types.payment_schedule_term

        return {
            "paymentScheduleTerm": aws_sdk_marketplace_agreement.types.payment_schedule_term.serialize_aws_json_1_0(
                value["paymentScheduleTerm"]
            )
        }
    elif "freeTrialPricingTerm" in value:
        import aws_sdk_marketplace_agreement.types.free_trial_pricing_term

        return {
            "freeTrialPricingTerm": aws_sdk_marketplace_agreement.types.free_trial_pricing_term.serialize_aws_json_1_0(
                value["freeTrialPricingTerm"]
            )
        }
    elif "fixedUpfrontPricingTerm" in value:
        import aws_sdk_marketplace_agreement.types.fixed_upfront_pricing_term

        return {
            "fixedUpfrontPricingTerm": aws_sdk_marketplace_agreement.types.fixed_upfront_pricing_term.serialize_aws_json_1_0(
                value["fixedUpfrontPricingTerm"]
            )
        }
    elif "variablePaymentTerm" in value:
        import aws_sdk_marketplace_agreement.types.variable_payment_term

        return {
            "variablePaymentTerm": aws_sdk_marketplace_agreement.types.variable_payment_term.serialize_aws_json_1_0(
                value["variablePaymentTerm"]
            )
        }
    else:
        raise SerializationError("AcceptedTerm: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AcceptedTerm:
    if "legalTerm" in data:
        import aws_sdk_marketplace_agreement.types.legal_term

        return {
            "legalTerm": aws_sdk_marketplace_agreement.types.legal_term.deserialize_aws_json_1_0(
                data["legalTerm"]
            )
        }
    elif "supportTerm" in data:
        import aws_sdk_marketplace_agreement.types.support_term

        return {
            "supportTerm": aws_sdk_marketplace_agreement.types.support_term.deserialize_aws_json_1_0(
                data["supportTerm"]
            )
        }
    elif "renewalTerm" in data:
        import aws_sdk_marketplace_agreement.types.renewal_term

        return {
            "renewalTerm": aws_sdk_marketplace_agreement.types.renewal_term.deserialize_aws_json_1_0(
                data["renewalTerm"]
            )
        }
    elif "usageBasedPricingTerm" in data:
        import aws_sdk_marketplace_agreement.types.usage_based_pricing_term

        return {
            "usageBasedPricingTerm": aws_sdk_marketplace_agreement.types.usage_based_pricing_term.deserialize_aws_json_1_0(
                data["usageBasedPricingTerm"]
            )
        }
    elif "configurableUpfrontPricingTerm" in data:
        import aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term

        return {
            "configurableUpfrontPricingTerm": aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term.deserialize_aws_json_1_0(
                data["configurableUpfrontPricingTerm"]
            )
        }
    elif "byolPricingTerm" in data:
        import aws_sdk_marketplace_agreement.types.byol_pricing_term

        return {
            "byolPricingTerm": aws_sdk_marketplace_agreement.types.byol_pricing_term.deserialize_aws_json_1_0(
                data["byolPricingTerm"]
            )
        }
    elif "recurringPaymentTerm" in data:
        import aws_sdk_marketplace_agreement.types.recurring_payment_term

        return {
            "recurringPaymentTerm": aws_sdk_marketplace_agreement.types.recurring_payment_term.deserialize_aws_json_1_0(
                data["recurringPaymentTerm"]
            )
        }
    elif "validityTerm" in data:
        import aws_sdk_marketplace_agreement.types.validity_term

        return {
            "validityTerm": aws_sdk_marketplace_agreement.types.validity_term.deserialize_aws_json_1_0(
                data["validityTerm"]
            )
        }
    elif "paymentScheduleTerm" in data:
        import aws_sdk_marketplace_agreement.types.payment_schedule_term

        return {
            "paymentScheduleTerm": aws_sdk_marketplace_agreement.types.payment_schedule_term.deserialize_aws_json_1_0(
                data["paymentScheduleTerm"]
            )
        }
    elif "freeTrialPricingTerm" in data:
        import aws_sdk_marketplace_agreement.types.free_trial_pricing_term

        return {
            "freeTrialPricingTerm": aws_sdk_marketplace_agreement.types.free_trial_pricing_term.deserialize_aws_json_1_0(
                data["freeTrialPricingTerm"]
            )
        }
    elif "fixedUpfrontPricingTerm" in data:
        import aws_sdk_marketplace_agreement.types.fixed_upfront_pricing_term

        return {
            "fixedUpfrontPricingTerm": aws_sdk_marketplace_agreement.types.fixed_upfront_pricing_term.deserialize_aws_json_1_0(
                data["fixedUpfrontPricingTerm"]
            )
        }
    elif "variablePaymentTerm" in data:
        import aws_sdk_marketplace_agreement.types.variable_payment_term

        return {
            "variablePaymentTerm": aws_sdk_marketplace_agreement.types.variable_payment_term.deserialize_aws_json_1_0(
                data["variablePaymentTerm"]
            )
        }
    else:
        raise DeserializationError("AcceptedTerm: no recognized variant key")
