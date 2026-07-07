"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#NegateSavingsPlanAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.uuid


class NegateSavingsPlanAction(TypedDict, closed=True):
    savings_plan_id: NotRequired["aws_sdk_bcm_pricing_calculator.types.uuid.Uuid"]
    """<p> The ID of the Savings Plan to remove. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NegateSavingsPlanAction) -> dict:
    out: dict = {}
    if "savings_plan_id" in value:
        out["savingsPlanId"] = value["savings_plan_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NegateSavingsPlanAction:
    out: NegateSavingsPlanAction = {}  # type: ignore[typeddict-item]
    if "savingsPlanId" in data:
        out["savings_plan_id"] = data["savingsPlanId"]
    return out
