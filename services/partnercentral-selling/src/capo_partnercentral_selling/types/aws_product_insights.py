"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductInsights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.amount_map
    import capo_partnercentral_selling.types.aws_products_list
    import capo_partnercentral_selling.types.currency_code
    import capo_partnercentral_selling.types.monetary_amount
    import capo_partnercentral_selling.types.payment_frequency


class AwsProductInsights(TypedDict, closed=True):
    currency_code: "capo_partnercentral_selling.types.currency_code.CurrencyCode"
    """<p>ISO 4217 currency code. Supported values are <code>USD</code> and <code>EUR</code>. Returns <code>EUR</code> when the opportunity is in the <code>aws-eusc</code> (AWS European Sovereign Cloud) partition.</p>"""
    frequency: "capo_partnercentral_selling.types.payment_frequency.PaymentFrequency"
    """<p>Time period for spend amounts.</p>"""
    total_amount: NotRequired[
        "capo_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Total estimated spend for this source before optimizations.</p>"""
    total_optimized_amount: NotRequired[
        "capo_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Total estimated spend after applying recommended optimizations.</p>"""
    total_potential_savings_amount: NotRequired[
        "capo_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Quantified savings achievable through implementing optimizations.</p>"""
    total_amount_by_category: "capo_partnercentral_selling.types.amount_map.AmountMap"
    """<p>Spend amounts mapped to AWS programs and modernization pathways.</p>"""
    aws_products: "capo_partnercentral_selling.types.aws_products_list.AwsProductsList"
    """<p>Product-level details including costs and optimization recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductInsights) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.currency_code

    out["CurrencyCode"] = (
        capo_partnercentral_selling.types.currency_code.serialize_aws_json_1_0(
            value["currency_code"]
        )
    )
    import capo_partnercentral_selling.types.payment_frequency

    out["Frequency"] = (
        capo_partnercentral_selling.types.payment_frequency.serialize_aws_json_1_0(
            value["frequency"]
        )
    )
    if "total_amount" in value:
        out["TotalAmount"] = value["total_amount"]
    if "total_optimized_amount" in value:
        out["TotalOptimizedAmount"] = value["total_optimized_amount"]
    if "total_potential_savings_amount" in value:
        out["TotalPotentialSavingsAmount"] = value["total_potential_savings_amount"]
    import capo_partnercentral_selling.types.amount_map

    out["TotalAmountByCategory"] = (
        capo_partnercentral_selling.types.amount_map.serialize_aws_json_1_0(
            value["total_amount_by_category"]
        )
    )
    import capo_partnercentral_selling.types.aws_products_list

    out["AwsProducts"] = (
        capo_partnercentral_selling.types.aws_products_list.serialize_aws_json_1_0(
            value["aws_products"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsProductInsights:
    out: AwsProductInsights = {}  # type: ignore[typeddict-item]
    if "CurrencyCode" in data:
        import capo_partnercentral_selling.types.currency_code

        out["currency_code"] = (
            capo_partnercentral_selling.types.currency_code.deserialize_aws_json_1_0(
                data["CurrencyCode"]
            )
        )
    else:
        raise DeserializationError("AwsProductInsights.currency_code required")
    if "Frequency" in data:
        import capo_partnercentral_selling.types.payment_frequency

        out["frequency"] = (
            capo_partnercentral_selling.types.payment_frequency.deserialize_aws_json_1_0(
                data["Frequency"]
            )
        )
    else:
        raise DeserializationError("AwsProductInsights.frequency required")
    if "TotalAmount" in data:
        out["total_amount"] = data["TotalAmount"]
    if "TotalOptimizedAmount" in data:
        out["total_optimized_amount"] = data["TotalOptimizedAmount"]
    if "TotalPotentialSavingsAmount" in data:
        out["total_potential_savings_amount"] = data["TotalPotentialSavingsAmount"]
    if "TotalAmountByCategory" in data:
        import capo_partnercentral_selling.types.amount_map

        out["total_amount_by_category"] = (
            capo_partnercentral_selling.types.amount_map.deserialize_aws_json_1_0(
                data["TotalAmountByCategory"]
            )
        )
    else:
        raise DeserializationError(
            "AwsProductInsights.total_amount_by_category required"
        )
    if "AwsProducts" in data:
        import capo_partnercentral_selling.types.aws_products_list

        out["aws_products"] = (
            capo_partnercentral_selling.types.aws_products_list.deserialize_aws_json_1_0(
                data["AwsProducts"]
            )
        )
    else:
        raise DeserializationError("AwsProductInsights.aws_products required")
    return out
