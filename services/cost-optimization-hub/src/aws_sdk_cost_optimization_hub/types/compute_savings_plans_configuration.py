"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ComputeSavingsPlansConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ComputeSavingsPlansConfiguration(TypedDict):
    account_scope: NotRequired["str"]
    """<p>The account scope for which you want recommendations. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to <code>PAYER</code>. If the value is <code>LINKED</code>, recommendations are calculated for individual member accounts only.</p>"""
    term: NotRequired["str"]
    """<p>The Savings Plans recommendation term in years.</p>"""
    payment_option: NotRequired["str"]
    """<p>The payment option for the commitment.</p>"""
    hourly_commitment: NotRequired["str"]
    """<p>The hourly commitment for the Savings Plans type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeSavingsPlansConfiguration) -> dict:
    out: dict = {}
    if "account_scope" in value:
        out["accountScope"] = value["account_scope"]
    if "term" in value:
        out["term"] = value["term"]
    if "payment_option" in value:
        out["paymentOption"] = value["payment_option"]
    if "hourly_commitment" in value:
        out["hourlyCommitment"] = value["hourly_commitment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ComputeSavingsPlansConfiguration:
    out: ComputeSavingsPlansConfiguration = {}  # type: ignore[typeddict-item]
    if "accountScope" in data:
        out["account_scope"] = data["accountScope"]
    if "term" in data:
        out["term"] = data["term"]
    if "paymentOption" in data:
        out["payment_option"] = data["paymentOption"]
    if "hourlyCommitment" in data:
        out["hourly_commitment"] = data["hourlyCommitment"]
    return out
