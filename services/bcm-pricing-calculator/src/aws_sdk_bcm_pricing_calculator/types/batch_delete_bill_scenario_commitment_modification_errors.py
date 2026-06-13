"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioCommitmentModificationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error

BatchDeleteBillScenarioCommitmentModificationErrors: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error.BatchDeleteBillScenarioCommitmentModificationError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchDeleteBillScenarioCommitmentModificationErrors,
) -> list:
    import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchDeleteBillScenarioCommitmentModificationErrors:
    import aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error

    out: BatchDeleteBillScenarioCommitmentModificationErrors = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.batch_delete_bill_scenario_commitment_modification_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
