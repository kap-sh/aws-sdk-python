"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#CreateBillScenarioRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_scenario_name
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.cost_category_arn
    import capo_bcm_pricing_calculator.types.group_sharing_preference_enum
    import capo_bcm_pricing_calculator.types.tags


class CreateBillScenarioRequest(TypedDict, closed=True):
    name: "capo_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
    """<p> A descriptive name for the bill scenario. </p>"""
    client_token: NotRequired[
        "capo_bcm_pricing_calculator.types.client_token.ClientToken"
    ]
    """<p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>"""
    tags: NotRequired["capo_bcm_pricing_calculator.types.tags.Tags"]
    """<p> The tags to apply to the bill scenario. </p>"""
    group_sharing_preference: NotRequired[
        "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
    ]
    """<p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>"""
    cost_category_group_sharing_preference_arn: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
    ]
    """<p>The arn of the cost category used in the reserved and prioritized group sharing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBillScenarioRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "tags" in value:
        import capo_bcm_pricing_calculator.types.tags

        out["tags"] = capo_bcm_pricing_calculator.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "group_sharing_preference" in value:
        import capo_bcm_pricing_calculator.types.group_sharing_preference_enum

        out["groupSharingPreference"] = (
            capo_bcm_pricing_calculator.types.group_sharing_preference_enum.serialize_aws_json_1_0(
                value["group_sharing_preference"]
            )
        )
    if "cost_category_group_sharing_preference_arn" in value:
        out["costCategoryGroupSharingPreferenceArn"] = value[
            "cost_category_group_sharing_preference_arn"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBillScenarioRequest:
    out: CreateBillScenarioRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateBillScenarioRequest.name required")
    if "tags" in data:
        import capo_bcm_pricing_calculator.types.tags

        out["tags"] = capo_bcm_pricing_calculator.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "groupSharingPreference" in data:
        import capo_bcm_pricing_calculator.types.group_sharing_preference_enum

        out["group_sharing_preference"] = (
            capo_bcm_pricing_calculator.types.group_sharing_preference_enum.deserialize_aws_json_1_0(
                data["groupSharingPreference"]
            )
        )
    if "costCategoryGroupSharingPreferenceArn" in data:
        out["cost_category_group_sharing_preference_arn"] = data[
            "costCategoryGroupSharingPreferenceArn"
        ]
    return out
