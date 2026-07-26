"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateInputCommitmentModificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.usage_group


class BillEstimateInputCommitmentModificationSummary(TypedDict, closed=True):
    id: NotRequired["capo_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier of the commitment modification. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The group identifier for the commitment modification. </p>"""
    usage_account_id: NotRequired[
        "capo_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with this commitment modification. </p>"""
    commitment_action: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.BillScenarioCommitmentModificationAction"
    ]
    """<p> The specific commitment action taken in this modification. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BillEstimateInputCommitmentModificationSummary,
) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "group" in value:
        out["group"] = value["group"]
    if "usage_account_id" in value:
        out["usageAccountId"] = value["usage_account_id"]
    if "commitment_action" in value:
        import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action

        out["commitmentAction"] = (
            capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.serialize_aws_json_1_0(
                value["commitment_action"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BillEstimateInputCommitmentModificationSummary:
    out: BillEstimateInputCommitmentModificationSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "group" in data:
        out["group"] = data["group"]
    if "usageAccountId" in data:
        out["usage_account_id"] = data["usageAccountId"]
    if "commitmentAction" in data:
        import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action

        out["commitment_action"] = (
            capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.deserialize_aws_json_1_0(
                data["commitmentAction"]
            )
        )
    return out
