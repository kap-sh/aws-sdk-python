"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioCommitmentModificationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.usage_group


class BatchUpdateBillScenarioCommitmentModificationEntry(TypedDict, closed=True):
    id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the commitment modification to update. </p>"""
    group: NotRequired["aws_sdk_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The updated group identifier for the commitment modification. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioCommitmentModificationEntry,
) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "group" in value:
        out["group"] = value["group"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchUpdateBillScenarioCommitmentModificationEntry:
    out: BatchUpdateBillScenarioCommitmentModificationEntry = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "BatchUpdateBillScenarioCommitmentModificationEntry.id required"
        )
    if "group" in data:
        out["group"] = data["group"]
    return out
