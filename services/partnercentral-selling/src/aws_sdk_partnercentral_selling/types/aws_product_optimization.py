"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductOptimization``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.monetary_amount


class AwsProductOptimization(TypedDict, closed=True):
    description: "str"
    """<p>Human-readable explanation of the optimization strategy.</p>"""
    savings_amount: (
        "aws_sdk_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    )
    """<p>Quantified cost savings achievable by implementing this optimization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductOptimization) -> dict:
    out: dict = {}
    out["Description"] = value["description"]
    out["SavingsAmount"] = value["savings_amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsProductOptimization:
    out: AwsProductOptimization = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("AwsProductOptimization.description required")
    if "SavingsAmount" in data:
        out["savings_amount"] = data["SavingsAmount"]
    else:
        raise DeserializationError("AwsProductOptimization.savings_amount required")
    return out
