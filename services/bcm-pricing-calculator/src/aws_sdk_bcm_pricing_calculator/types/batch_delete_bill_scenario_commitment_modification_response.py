"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioCommitmentModificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_errors


class BatchDeleteBillScenarioCommitmentModificationResponse(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_errors.BatchDeleteBillScenarioCommitmentModificationErrors"
    ]
    """<p> Returns the list of errors reason and the commitment item keys that cannot be deleted from the Bill Scenario. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchDeleteBillScenarioCommitmentModificationResponse,
) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_errors

        out["errors"] = (
            aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchDeleteBillScenarioCommitmentModificationResponse:
    out: BatchDeleteBillScenarioCommitmentModificationResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_errors

        out["errors"] = (
            aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
