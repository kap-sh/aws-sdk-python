"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioCommitmentModificationEntries``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.resource_id

BatchDeleteBillScenarioCommitmentModificationEntries: TypeAlias = list["aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchDeleteBillScenarioCommitmentModificationEntries) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BatchDeleteBillScenarioCommitmentModificationEntries:
    return list(data)