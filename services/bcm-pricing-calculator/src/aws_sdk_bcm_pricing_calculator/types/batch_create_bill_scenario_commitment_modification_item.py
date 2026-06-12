"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.account_id
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action
    import aws_sdk_bcm_pricing_calculator.types.key
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.usage_group

class BatchCreateBillScenarioCommitmentModificationItem(TypedDict):
    key: NotRequired["aws_sdk_bcm_pricing_calculator.types.key.Key"]
    """<p> The key of the successfully created entry. This can be any valid string. This key is useful to identify errors associated with any commitment entry as any error is returned with this key. </p>"""
    id: NotRequired["aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier assigned to the created commitment modification. </p>"""
    group: NotRequired["aws_sdk_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The group identifier for the created commitment modification. </p>"""
    usage_account_id: NotRequired["aws_sdk_bcm_pricing_calculator.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID associated with the created commitment modification. </p>"""
    commitment_action: NotRequired["aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.BillScenarioCommitmentModificationAction"]
    """<p> The specific commitment action that was taken. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillScenarioCommitmentModificationItem) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "id" in value:
        out["id"] = value["id"]
    if "group" in value:
        out["group"] = value["group"]
    if "usage_account_id" in value:
        out["usageAccountId"] = value["usage_account_id"]
    if "commitment_action" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action
        out["commitmentAction"] = aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.serialize_aws_json_1_0(value["commitment_action"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillScenarioCommitmentModificationItem:
    out: BatchCreateBillScenarioCommitmentModificationItem = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "id" in data:
        out["id"] = data["id"]
    if "group" in data:
        out["group"] = data["group"]
    if "usageAccountId" in data:
        out["usage_account_id"] = data["usageAccountId"]
    if "commitmentAction" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action
        out["commitment_action"] = aws_sdk_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.deserialize_aws_json_1_0(data["commitmentAction"])
    return out