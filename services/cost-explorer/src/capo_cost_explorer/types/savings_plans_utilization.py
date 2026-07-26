"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansUtilization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class SavingsPlansUtilization(TypedDict, closed=True):
    total_commitment: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The total amount of Savings Plans commitment that's been purchased in an account (or set of accounts).</p>"""
    used_commitment: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The amount of your Savings Plans commitment that was consumed from Savings Plans eligible usage in a specific period.</p>"""
    unused_commitment: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The amount of your Savings Plans commitment that wasn't consumed from Savings Plans eligible usage in a specific period.</p>"""
    utilization_percentage: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The amount of <code>UsedCommitment</code> divided by the <code>TotalCommitment</code> for your Savings Plans.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansUtilization) -> dict:
    out: dict = {}
    if "total_commitment" in value:
        out["TotalCommitment"] = value["total_commitment"]
    if "used_commitment" in value:
        out["UsedCommitment"] = value["used_commitment"]
    if "unused_commitment" in value:
        out["UnusedCommitment"] = value["unused_commitment"]
    if "utilization_percentage" in value:
        out["UtilizationPercentage"] = value["utilization_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansUtilization:
    out: SavingsPlansUtilization = {}  # type: ignore[typeddict-item]
    if "TotalCommitment" in data:
        out["total_commitment"] = data["TotalCommitment"]
    if "UsedCommitment" in data:
        out["used_commitment"] = data["UsedCommitment"]
    if "UnusedCommitment" in data:
        out["unused_commitment"] = data["UnusedCommitment"]
    if "UtilizationPercentage" in data:
        out["utilization_percentage"] = data["UtilizationPercentage"]
    return out
