"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#GetBillEstimateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_cost_summary
    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_name
    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_status
    import aws_sdk_bcm_pricing_calculator.types.bill_interval
    import aws_sdk_bcm_pricing_calculator.types.cost_category_arn
    import aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class GetBillEstimateResponse(TypedDict, closed=True):
    id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the retrieved bill estimate. </p>"""
    name: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
    ]
    """<p> The name of the retrieved bill estimate. </p>"""
    status: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_estimate_status.BillEstimateStatus"
    ]
    """<p> The current status of the bill estimate. </p>"""
    failure_message: NotRequired["str"]
    """<p> An error message if the bill estimate retrieval failed. </p>"""
    bill_interval: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_interval.BillInterval"
    ]
    """<p> The time period covered by the bill estimate. </p>"""
    cost_summary: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_estimate_cost_summary.BillEstimateCostSummary"
    ]
    """<p> A summary of the estimated costs. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill estimate was created. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill estimate will expire. </p>"""
    group_sharing_preference: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
    ]
    """<p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>"""
    cost_category_group_sharing_preference_arn: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
    ]
    """<p>The arn of the cost category used in the reserved and prioritized group sharing.</p>"""
    cost_category_group_sharing_preference_effective_date: NotRequired[
        "datetime.datetime"
    ]
    """<p>Timestamp of the effective date of the cost category used in the group sharing settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillEstimateResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_estimate_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_estimate_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "bill_interval" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_interval

        out["billInterval"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_interval.serialize_aws_json_1_0(
                value["bill_interval"]
            )
        )
    if "cost_summary" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_estimate_cost_summary

        out["costSummary"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_estimate_cost_summary.serialize_aws_json_1_0(
                value["cost_summary"]
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
    if "cost_category_group_sharing_preference_effective_date" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["costCategoryGroupSharingPreferenceEffectiveDate"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["cost_category_group_sharing_preference_effective_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillEstimateResponse:
    out: GetBillEstimateResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetBillEstimateResponse.id required")
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_estimate_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_estimate_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "billInterval" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_interval

        out["bill_interval"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_interval.deserialize_aws_json_1_0(
                data["billInterval"]
            )
        )
    if "costSummary" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_estimate_cost_summary

        out["cost_summary"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_estimate_cost_summary.deserialize_aws_json_1_0(
                data["costSummary"]
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
    if "costCategoryGroupSharingPreferenceEffectiveDate" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["cost_category_group_sharing_preference_effective_date"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["costCategoryGroupSharingPreferenceEffectiveDate"]
            )
        )
    return out
