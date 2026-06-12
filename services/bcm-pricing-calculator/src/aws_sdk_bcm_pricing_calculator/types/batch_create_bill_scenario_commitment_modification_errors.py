"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationErrors``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error

BatchCreateBillScenarioCommitmentModificationErrors: TypeAlias = list["aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error.BatchCreateBillScenarioCommitmentModificationError"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillScenarioCommitmentModificationErrors) -> list:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error
    out: list = []
    for item in value:
        out.append(aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BatchCreateBillScenarioCommitmentModificationErrors:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error
    out: BatchCreateBillScenarioCommitmentModificationErrors = []
    for item in data:
        out.append(aws_sdk_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_error.deserialize_aws_json_1_0(item))
    return out