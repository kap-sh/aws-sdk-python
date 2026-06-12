"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioCommitmentModificationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_errors
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items

class BatchUpdateBillScenarioCommitmentModificationResponse(TypedDict):
    items: NotRequired["aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items.BillScenarioCommitmentModificationItems"]
    """<p> Returns the list of successful commitment line items that were updated for a Bill Scenario. </p>"""
    errors: NotRequired["aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_errors.BatchUpdateBillScenarioCommitmentModificationErrors"]
    """<p> Returns the list of error reasons and commitment line item IDs that could not be updated for the Bill Scenario. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateBillScenarioCommitmentModificationResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items
        out["items"] = aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items.serialize_aws_json_1_0(value["items"])
    if "errors" in value:
        import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_errors
        out["errors"] = aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_errors.serialize_aws_json_1_0(value["errors"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchUpdateBillScenarioCommitmentModificationResponse:
    out: BatchUpdateBillScenarioCommitmentModificationResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items
        out["items"] = aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items.deserialize_aws_json_1_0(data["items"])
    if "errors" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_errors
        out["errors"] = aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_errors.deserialize_aws_json_1_0(data["errors"])
    return out