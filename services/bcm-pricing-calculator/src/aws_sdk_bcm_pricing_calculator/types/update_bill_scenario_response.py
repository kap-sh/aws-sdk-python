"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UpdateBillScenarioResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bcm_pricing_calculator.types.bill_interval
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_name
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_status
    import aws_sdk_bcm_pricing_calculator.types.cost_category_arn
    import aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class UpdateBillScenarioResponse(TypedDict, closed=True):
    id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the updated bill scenario. </p>"""
    name: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
    ]
    """<p> The updated name of the bill scenario. </p>"""
    bill_interval: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_interval.BillInterval"
    ]
    """<p> The time period covered by the updated bill scenario. </p>"""
    status: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_scenario_status.BillScenarioStatus"
    ]
    """<p> The current status of the updated bill scenario. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill scenario was originally created. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The updated expiration timestamp for the bill scenario. </p>"""
    failure_message: NotRequired["str"]
    """<p> An error message if the bill scenario update failed. </p>"""
    group_sharing_preference: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
    ]
    """<p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>"""
    cost_category_group_sharing_preference_arn: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
    ]
    """<p>The arn of the cost category used in the reserved and prioritized group sharing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBillScenarioResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "bill_interval" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_interval

        out["billInterval"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_interval.serialize_aws_json_1_0(
                value["bill_interval"]
            )
        )
    if "status" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_scenario_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_scenario_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_at" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "expires_at" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["expiresAt"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
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


def deserialize_aws_json_1_0(data: dict) -> UpdateBillScenarioResponse:
    out: UpdateBillScenarioResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateBillScenarioResponse.id required")
    if "name" in data:
        out["name"] = data["name"]
    if "billInterval" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_interval

        out["bill_interval"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_interval.deserialize_aws_json_1_0(
                data["billInterval"]
            )
        )
    if "status" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_scenario_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_scenario_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "expiresAt" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["expires_at"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
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
