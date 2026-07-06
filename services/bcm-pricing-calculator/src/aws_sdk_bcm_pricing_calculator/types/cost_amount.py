"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#CostAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.currency_code


class CostAmount(TypedDict, closed=True):
    amount: NotRequired["float"]
    """<p> The numeric value of the cost. </p>"""
    currency: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.currency_code.CurrencyCode"
    ]
    """<p> The currency code for the cost amount. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CostAmount) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "currency" in value:
        import aws_sdk_bcm_pricing_calculator.types.currency_code

        out["currency"] = (
            aws_sdk_bcm_pricing_calculator.types.currency_code.serialize_aws_json_1_0(
                value["currency"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CostAmount:
    out: CostAmount = {}  # type: ignore[typeddict-item]
    if "amount" in data:
        out["amount"] = data["amount"]
    if "currency" in data:
        import aws_sdk_bcm_pricing_calculator.types.currency_code

        out["currency"] = (
            aws_sdk_bcm_pricing_calculator.types.currency_code.deserialize_aws_json_1_0(
                data["currency"]
            )
        )
    return out
