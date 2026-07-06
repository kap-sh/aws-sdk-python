"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2InstanceSavingsPlansConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class Ec2InstanceSavingsPlansConfiguration(TypedDict, closed=True):
    account_scope: NotRequired["str"]
    """<p>The account scope for which you want recommendations.</p>"""
    term: NotRequired["str"]
    """<p>The Savings Plans recommendation term in years.</p>"""
    payment_option: NotRequired["str"]
    """<p>The payment option for the commitment.</p>"""
    hourly_commitment: NotRequired["str"]
    """<p>The hourly commitment for the Savings Plans type.</p>"""
    instance_family: NotRequired["str"]
    """<p>The instance family of the recommended Savings Plans.</p>"""
    savings_plans_region: NotRequired["str"]
    """<p>The Amazon Web Services Region of the commitment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2InstanceSavingsPlansConfiguration) -> dict:
    out: dict = {}
    if "account_scope" in value:
        out["accountScope"] = value["account_scope"]
    if "term" in value:
        out["term"] = value["term"]
    if "payment_option" in value:
        out["paymentOption"] = value["payment_option"]
    if "hourly_commitment" in value:
        out["hourlyCommitment"] = value["hourly_commitment"]
    if "instance_family" in value:
        out["instanceFamily"] = value["instance_family"]
    if "savings_plans_region" in value:
        out["savingsPlansRegion"] = value["savings_plans_region"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2InstanceSavingsPlansConfiguration:
    out: Ec2InstanceSavingsPlansConfiguration = {}  # type: ignore[typeddict-item]
    if "accountScope" in data:
        out["account_scope"] = data["accountScope"]
    if "term" in data:
        out["term"] = data["term"]
    if "paymentOption" in data:
        out["payment_option"] = data["paymentOption"]
    if "hourlyCommitment" in data:
        out["hourly_commitment"] = data["hourlyCommitment"]
    if "instanceFamily" in data:
        out["instance_family"] = data["instanceFamily"]
    if "savingsPlansRegion" in data:
        out["savings_plans_region"] = data["savingsPlansRegion"]
    return out
