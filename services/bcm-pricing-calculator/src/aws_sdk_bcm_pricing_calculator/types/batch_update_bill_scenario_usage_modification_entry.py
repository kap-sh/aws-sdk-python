"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioUsageModificationEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bcm_pricing_calculator.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.usage_amounts
    import aws_sdk_bcm_pricing_calculator.types.usage_group

class BatchUpdateBillScenarioUsageModificationEntry(TypedDict):
    id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the usage modification to update. </p>"""
    group: NotRequired["aws_sdk_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The updated group identifier for the usage modification. </p>"""
    amounts: NotRequired["aws_sdk_bcm_pricing_calculator.types.usage_amounts.UsageAmounts"]
    """<p> The updated usage amounts for the modification. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateBillScenarioUsageModificationEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "group" in value:
        out["group"] = value["group"]
    if "amounts" in value:
        import aws_sdk_bcm_pricing_calculator.types.usage_amounts
        out["amounts"] = aws_sdk_bcm_pricing_calculator.types.usage_amounts.serialize_aws_json_1_0(value["amounts"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchUpdateBillScenarioUsageModificationEntry:
    out: BatchUpdateBillScenarioUsageModificationEntry = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("BatchUpdateBillScenarioUsageModificationEntry.id required")
    if "group" in data:
        out["group"] = data["group"]
    if "amounts" in data:
        import aws_sdk_bcm_pricing_calculator.types.usage_amounts
        out["amounts"] = aws_sdk_bcm_pricing_calculator.types.usage_amounts.deserialize_aws_json_1_0(data["amounts"])
    return out