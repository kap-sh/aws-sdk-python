"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansAmortizedCommitment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class SavingsPlansAmortizedCommitment(TypedDict):
    amortized_recurring_commitment: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The amortized amount of your Savings Plans commitment that was purchased with either a <code>Partial</code> or a <code>NoUpfront</code>.</p>"""
    amortized_upfront_commitment: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The amortized amount of your Savings Plans commitment that was purchased with an <code>Upfront</code> or <code>PartialUpfront</code> Savings Plans.</p>"""
    total_amortized_commitment: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The total amortized amount of your Savings Plans commitment, regardless of your Savings Plans purchase method. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansAmortizedCommitment) -> dict:
    out: dict = {}
    if "amortized_recurring_commitment" in value:
        out["AmortizedRecurringCommitment"] = value["amortized_recurring_commitment"]
    if "amortized_upfront_commitment" in value:
        out["AmortizedUpfrontCommitment"] = value["amortized_upfront_commitment"]
    if "total_amortized_commitment" in value:
        out["TotalAmortizedCommitment"] = value["total_amortized_commitment"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansAmortizedCommitment:
    out: SavingsPlansAmortizedCommitment = {}  # type: ignore[typeddict-item]
    if "AmortizedRecurringCommitment" in data:
        out["amortized_recurring_commitment"] = data["AmortizedRecurringCommitment"]
    if "AmortizedUpfrontCommitment" in data:
        out["amortized_upfront_commitment"] = data["AmortizedUpfrontCommitment"]
    if "TotalAmortizedCommitment" in data:
        out["total_amortized_commitment"] = data["TotalAmortizedCommitment"]
    return out
