"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_errors
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_items


class BatchCreateBillScenarioCommitmentModificationResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_items.BatchCreateBillScenarioCommitmentModificationItems"
    ]
    """<p> Returns the list of successful commitment line items that were created for the Bill Scenario. </p>"""
    errors: NotRequired[
        "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_errors.BatchCreateBillScenarioCommitmentModificationErrors"
    ]
    """<p> Returns the list of errors reason and the commitment item keys that cannot be created in the Bill Scenario. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioCommitmentModificationResponse,
) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_items

        out["items"] = (
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_items.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "errors" in value:
        import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_errors

        out["errors"] = (
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchCreateBillScenarioCommitmentModificationResponse:
    out: BatchCreateBillScenarioCommitmentModificationResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_items

        out["items"] = (
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_items.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "errors" in data:
        import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_errors

        out["errors"] = (
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
