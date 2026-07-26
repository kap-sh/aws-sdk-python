"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlans``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.payment_option
    import capo_cost_explorer.types.savings_plans_commitment
    import capo_cost_explorer.types.supported_savings_plans_type
    import capo_cost_explorer.types.term_in_years


class SavingsPlans(TypedDict, closed=True):
    payment_option: NotRequired["capo_cost_explorer.types.payment_option.PaymentOption"]
    """<p>The payment option for the Savings Plans commitment.</p>"""
    savings_plans_type: NotRequired[
        "capo_cost_explorer.types.supported_savings_plans_type.SupportedSavingsPlansType"
    ]
    """<p>The Savings Plans type.</p>"""
    region: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The Region associated with the Savings Plans commitment.</p>"""
    instance_family: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The instance family of the Savings Plans commitment.</p>"""
    term_in_years: NotRequired["capo_cost_explorer.types.term_in_years.TermInYears"]
    """<p>The term that you want the Savings Plans commitment for.</p>"""
    savings_plans_commitment: NotRequired[
        "capo_cost_explorer.types.savings_plans_commitment.SavingsPlansCommitment"
    ]
    """<p>The Savings Plans commitment.</p>"""
    offering_id: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The unique ID that's used to distinguish Savings Plans commitments from one another.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlans) -> dict:
    out: dict = {}
    if "payment_option" in value:
        import capo_cost_explorer.types.payment_option

        out["PaymentOption"] = (
            capo_cost_explorer.types.payment_option.serialize_aws_json_1_1(
                value["payment_option"]
            )
        )
    if "savings_plans_type" in value:
        import capo_cost_explorer.types.supported_savings_plans_type

        out["SavingsPlansType"] = (
            capo_cost_explorer.types.supported_savings_plans_type.serialize_aws_json_1_1(
                value["savings_plans_type"]
            )
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "instance_family" in value:
        out["InstanceFamily"] = value["instance_family"]
    if "term_in_years" in value:
        import capo_cost_explorer.types.term_in_years

        out["TermInYears"] = (
            capo_cost_explorer.types.term_in_years.serialize_aws_json_1_1(
                value["term_in_years"]
            )
        )
    if "savings_plans_commitment" in value:
        out["SavingsPlansCommitment"] = value["savings_plans_commitment"]
    if "offering_id" in value:
        out["OfferingId"] = value["offering_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlans:
    out: SavingsPlans = {}  # type: ignore[typeddict-item]
    if "PaymentOption" in data:
        import capo_cost_explorer.types.payment_option

        out["payment_option"] = (
            capo_cost_explorer.types.payment_option.deserialize_aws_json_1_1(
                data["PaymentOption"]
            )
        )
    if "SavingsPlansType" in data:
        import capo_cost_explorer.types.supported_savings_plans_type

        out["savings_plans_type"] = (
            capo_cost_explorer.types.supported_savings_plans_type.deserialize_aws_json_1_1(
                data["SavingsPlansType"]
            )
        )
    if "Region" in data:
        out["region"] = data["Region"]
    if "InstanceFamily" in data:
        out["instance_family"] = data["InstanceFamily"]
    if "TermInYears" in data:
        import capo_cost_explorer.types.term_in_years

        out["term_in_years"] = (
            capo_cost_explorer.types.term_in_years.deserialize_aws_json_1_1(
                data["TermInYears"]
            )
        )
    if "SavingsPlansCommitment" in data:
        out["savings_plans_commitment"] = data["SavingsPlansCommitment"]
    if "OfferingId" in data:
        out["offering_id"] = data["OfferingId"]
    return out
