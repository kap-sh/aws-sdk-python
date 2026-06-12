"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bcm_pricing_calculator.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries
    import aws_sdk_bcm_pricing_calculator.types.client_token
    import aws_sdk_bcm_pricing_calculator.types.resource_id

class BatchCreateBillScenarioCommitmentModificationRequest(TypedDict):
    bill_scenario_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to create the modeled commitment. </p>"""
    commitment_modifications: "aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries.BatchCreateBillScenarioCommitmentModificationEntries"
    """<p> List of commitments that you want to model in the Bill Scenario. </p>"""
    client_token: NotRequired["aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"]
    """<p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillScenarioCommitmentModificationRequest) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries
    out["commitmentModifications"] = aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries.serialize_aws_json_1_0(value["commitment_modifications"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillScenarioCommitmentModificationRequest:
    out: BatchCreateBillScenarioCommitmentModificationRequest = {}  # type: ignore[typeddict-item]
    if "billScenarioId" in data:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        raise DeserializationError("BatchCreateBillScenarioCommitmentModificationRequest.bill_scenario_id required")
    if "commitmentModifications" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries
        out["commitment_modifications"] = aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries.deserialize_aws_json_1_0(data["commitmentModifications"])
    else:
        raise DeserializationError("BatchCreateBillScenarioCommitmentModificationRequest.commitment_modifications required")
    return out