"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error_code
    import capo_bcm_pricing_calculator.types.key


class BatchCreateBillScenarioCommitmentModificationError(TypedDict, closed=True):
    key: NotRequired["capo_bcm_pricing_calculator.types.key.Key"]
    """<p> The key of the entry that caused the error. </p>"""
    error_message: NotRequired["str"]
    """<p> A descriptive message for the error that occurred. </p>"""
    error_code: NotRequired[
        "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error_code.BatchCreateBillScenarioCommitmentModificationErrorCode"
    ]
    """<p> The error code associated with the failed operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioCommitmentModificationError,
) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error_code

        out["errorCode"] = (
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error_code.serialize_aws_json_1_0(
                value["error_code"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchCreateBillScenarioCommitmentModificationError:
    out: BatchCreateBillScenarioCommitmentModificationError = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error_code

        out["error_code"] = (
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error_code.deserialize_aws_json_1_0(
                data["errorCode"]
            )
        )
    return out
