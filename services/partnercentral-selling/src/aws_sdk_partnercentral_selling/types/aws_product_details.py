"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_product_optimizations_list
    import aws_sdk_partnercentral_selling.types.monetary_amount
    import aws_sdk_partnercentral_selling.types.string_list


class AwsProductDetails(TypedDict):
    product_code: "str"
    """<p>AWS Partner Central product identifier used for opportunity association.</p>"""
    service_code: NotRequired["str"]
    """<p>Pricing Calculator service code.</p>"""
    categories: "aws_sdk_partnercentral_selling.types.string_list.StringList"
    """<p>List of program and pathway categories this product is eligible for.</p>"""
    amount: NotRequired[
        "aws_sdk_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Baseline service cost before optimizations.</p>"""
    optimized_amount: NotRequired[
        "aws_sdk_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Service cost after applying optimizations.</p>"""
    potential_savings_amount: NotRequired[
        "aws_sdk_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    ]
    """<p>Service-specific cost reduction through optimizations.</p>"""
    optimizations: "aws_sdk_partnercentral_selling.types.aws_product_optimizations_list.AwsProductOptimizationsList"
    """<p>List of specific optimization recommendations for this product.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductDetails) -> dict:
    out: dict = {}
    out["ProductCode"] = value["product_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    import aws_sdk_partnercentral_selling.types.string_list

    out["Categories"] = (
        aws_sdk_partnercentral_selling.types.string_list.serialize_aws_json_1_0(
            value["categories"]
        )
    )
    if "amount" in value:
        out["Amount"] = value["amount"]
    if "optimized_amount" in value:
        out["OptimizedAmount"] = value["optimized_amount"]
    if "potential_savings_amount" in value:
        out["PotentialSavingsAmount"] = value["potential_savings_amount"]
    import aws_sdk_partnercentral_selling.types.aws_product_optimizations_list

    out["Optimizations"] = (
        aws_sdk_partnercentral_selling.types.aws_product_optimizations_list.serialize_aws_json_1_0(
            value["optimizations"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsProductDetails:
    out: AwsProductDetails = {}  # type: ignore[typeddict-item]
    if "ProductCode" in data:
        out["product_code"] = data["ProductCode"]
    else:
        raise DeserializationError("AwsProductDetails.product_code required")
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "Categories" in data:
        import aws_sdk_partnercentral_selling.types.string_list

        out["categories"] = (
            aws_sdk_partnercentral_selling.types.string_list.deserialize_aws_json_1_0(
                data["Categories"]
            )
        )
    else:
        raise DeserializationError("AwsProductDetails.categories required")
    if "Amount" in data:
        out["amount"] = data["Amount"]
    if "OptimizedAmount" in data:
        out["optimized_amount"] = data["OptimizedAmount"]
    if "PotentialSavingsAmount" in data:
        out["potential_savings_amount"] = data["PotentialSavingsAmount"]
    if "Optimizations" in data:
        import aws_sdk_partnercentral_selling.types.aws_product_optimizations_list

        out["optimizations"] = (
            aws_sdk_partnercentral_selling.types.aws_product_optimizations_list.deserialize_aws_json_1_0(
                data["Optimizations"]
            )
        )
    else:
        raise DeserializationError("AwsProductDetails.optimizations required")
    return out
