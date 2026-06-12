"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioCommitmentModificationError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error_code
    import aws_sdk_bcm_pricing_calculator.types.resource_id

class BatchDeleteBillScenarioCommitmentModificationError(TypedDict):
    id: NotRequired["aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The ID of the error. </p>"""
    error_code: NotRequired["aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error_code.BatchDeleteBillScenarioCommitmentModificationErrorCode"]
    """<p> The code associated with the error. </p>"""
    error_message: NotRequired["str"]
    """<p> The message that describes the error. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchDeleteBillScenarioCommitmentModificationError) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "error_code" in value:
        import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error_code
        out["errorCode"] = aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error_code.serialize_aws_json_1_0(value["error_code"])
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchDeleteBillScenarioCommitmentModificationError:
    out: BatchDeleteBillScenarioCommitmentModificationError = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "errorCode" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error_code
        out["error_code"] = aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error_code.deserialize_aws_json_1_0(data["errorCode"])
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out