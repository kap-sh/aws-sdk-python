"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UpdateBillScenarioRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_name
    import aws_sdk_bcm_pricing_calculator.types.cost_category_arn
    import aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class UpdateBillScenarioRequest(TypedDict):
    identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill scenario to update. </p>"""
    name: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
    ]
    """<p> The new name for the bill scenario. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The new expiration date for the bill scenario. </p>"""
    group_sharing_preference: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
    ]
    """<p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>"""
    cost_category_group_sharing_preference_arn: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
    ]
    """<p>The arn of the cost category used in the reserved and prioritized group sharing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBillScenarioRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "name" in value:
        out["name"] = value["name"]
    if "expires_at" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["expiresAt"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    if "group_sharing_preference" in value:
        import aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum

        out["groupSharingPreference"] = (
            aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.serialize_aws_json_1_0(
                value["group_sharing_preference"]
            )
        )
    if "cost_category_group_sharing_preference_arn" in value:
        out["costCategoryGroupSharingPreferenceArn"] = value[
            "cost_category_group_sharing_preference_arn"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBillScenarioRequest:
    out: UpdateBillScenarioRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("UpdateBillScenarioRequest.identifier required")
    if "name" in data:
        out["name"] = data["name"]
    if "expiresAt" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["expires_at"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    if "groupSharingPreference" in data:
        import aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum

        out["group_sharing_preference"] = (
            aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.deserialize_aws_json_1_0(
                data["groupSharingPreference"]
            )
        )
    if "costCategoryGroupSharingPreferenceArn" in data:
        out["cost_category_group_sharing_preference_arn"] = data[
            "costCategoryGroupSharingPreferenceArn"
        ]
    return out
