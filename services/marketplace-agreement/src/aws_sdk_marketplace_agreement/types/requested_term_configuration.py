"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RequestedTermConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_marketplace_agreement.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term_configuration
    import aws_sdk_marketplace_agreement.types.renewal_term_configuration
    import aws_sdk_marketplace_agreement.types.variable_payment_term_configuration


class _RequestedTermConfiguration_configurableUpfrontPricingTermConfiguration(
    TypedDict, closed=True
):
    configurableUpfrontPricingTermConfiguration: "aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term_configuration.ConfigurableUpfrontPricingTermConfiguration"


class _RequestedTermConfiguration_renewalTermConfiguration(TypedDict, closed=True):
    renewalTermConfiguration: "aws_sdk_marketplace_agreement.types.renewal_term_configuration.RenewalTermConfiguration"


class _RequestedTermConfiguration_variablePaymentTermConfiguration(
    TypedDict, closed=True
):
    variablePaymentTermConfiguration: "aws_sdk_marketplace_agreement.types.variable_payment_term_configuration.VariablePaymentTermConfiguration"


RequestedTermConfiguration: TypeAlias = (
    _RequestedTermConfiguration_configurableUpfrontPricingTermConfiguration
    | _RequestedTermConfiguration_renewalTermConfiguration
    | _RequestedTermConfiguration_variablePaymentTermConfiguration
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestedTermConfiguration) -> dict:
    if "configurableUpfrontPricingTermConfiguration" in value:
        import aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term_configuration

        return {
            "configurableUpfrontPricingTermConfiguration": aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term_configuration.serialize_aws_json_1_0(
                value["configurableUpfrontPricingTermConfiguration"]
            )
        }
    elif "renewalTermConfiguration" in value:
        import aws_sdk_marketplace_agreement.types.renewal_term_configuration

        return {
            "renewalTermConfiguration": aws_sdk_marketplace_agreement.types.renewal_term_configuration.serialize_aws_json_1_0(
                value["renewalTermConfiguration"]
            )
        }
    elif "variablePaymentTermConfiguration" in value:
        import aws_sdk_marketplace_agreement.types.variable_payment_term_configuration

        return {
            "variablePaymentTermConfiguration": aws_sdk_marketplace_agreement.types.variable_payment_term_configuration.serialize_aws_json_1_0(
                value["variablePaymentTermConfiguration"]
            )
        }
    else:
        raise SerializationError("RequestedTermConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RequestedTermConfiguration:
    if "configurableUpfrontPricingTermConfiguration" in data:
        import aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term_configuration

        return {
            "configurableUpfrontPricingTermConfiguration": aws_sdk_marketplace_agreement.types.configurable_upfront_pricing_term_configuration.deserialize_aws_json_1_0(
                data["configurableUpfrontPricingTermConfiguration"]
            )
        }
    elif "renewalTermConfiguration" in data:
        import aws_sdk_marketplace_agreement.types.renewal_term_configuration

        return {
            "renewalTermConfiguration": aws_sdk_marketplace_agreement.types.renewal_term_configuration.deserialize_aws_json_1_0(
                data["renewalTermConfiguration"]
            )
        }
    elif "variablePaymentTermConfiguration" in data:
        import aws_sdk_marketplace_agreement.types.variable_payment_term_configuration

        return {
            "variablePaymentTermConfiguration": aws_sdk_marketplace_agreement.types.variable_payment_term_configuration.deserialize_aws_json_1_0(
                data["variablePaymentTermConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "RequestedTermConfiguration: no recognized variant key"
        )
