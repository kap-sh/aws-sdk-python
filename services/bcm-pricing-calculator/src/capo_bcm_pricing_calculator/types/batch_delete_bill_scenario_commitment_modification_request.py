"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioCommitmentModificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_entries
    import capo_bcm_pricing_calculator.types.resource_id


class BatchDeleteBillScenarioCommitmentModificationRequest(TypedDict, closed=True):
    bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to delete the modeled commitment. </p>"""
    ids: "capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_entries.BatchDeleteBillScenarioCommitmentModificationEntries"
    """<p> List of commitments that you want to delete from the Bill Scenario. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchDeleteBillScenarioCommitmentModificationRequest,
) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_entries

    out["ids"] = (
        capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_entries.serialize_aws_json_1_0(
            value["ids"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchDeleteBillScenarioCommitmentModificationRequest:
    out: BatchDeleteBillScenarioCommitmentModificationRequest = {}  # type: ignore[typeddict-item]
    if "billScenarioId" in data:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        raise DeserializationError(
            "BatchDeleteBillScenarioCommitmentModificationRequest.bill_scenario_id required"
        )
    if "ids" in data:
        import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_entries

        out["ids"] = (
            capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_entries.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteBillScenarioCommitmentModificationRequest.ids required"
        )
    return out
