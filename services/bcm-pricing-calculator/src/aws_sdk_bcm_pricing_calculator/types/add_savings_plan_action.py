"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#AddSavingsPlanAction``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.savings_plan_commitment
    import aws_sdk_bcm_pricing_calculator.types.uuid

class AddSavingsPlanAction(TypedDict):
    savings_plan_offering_id: NotRequired["aws_sdk_bcm_pricing_calculator.types.uuid.Uuid"]
    """<p> The ID of the Savings Plan offering to add. For more information, see <a href=\"https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlansOfferings.html\"> DescribeSavingsPlansOfferings</a>. </p>"""
    commitment: NotRequired["aws_sdk_bcm_pricing_calculator.types.savings_plan_commitment.SavingsPlanCommitment"]
    """<p> The hourly commitment, in the same currency of the <code>savingsPlanOfferingId</code>. This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddSavingsPlanAction) -> dict:
    out: dict = {}
    if "savings_plan_offering_id" in value:
        out["savingsPlanOfferingId"] = value["savings_plan_offering_id"]
    if "commitment" in value:
        out["commitment"] = value["commitment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AddSavingsPlanAction:
    out: AddSavingsPlanAction = {}  # type: ignore[typeddict-item]
    if "savingsPlanOfferingId" in data:
        out["savings_plan_offering_id"] = data["savingsPlanOfferingId"]
    if "commitment" in data:
        out["commitment"] = data["commitment"]
    return out