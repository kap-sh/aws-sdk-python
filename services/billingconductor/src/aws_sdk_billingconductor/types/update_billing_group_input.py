"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateBillingGroupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.billing_group_description
    import aws_sdk_billingconductor.types.billing_group_name
    import aws_sdk_billingconductor.types.billing_group_status
    import aws_sdk_billingconductor.types.computation_preference
    import aws_sdk_billingconductor.types.update_billing_group_account_grouping


class UpdateBillingGroupInput(TypedDict):
    arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p>The Amazon Resource Name (ARN) of the billing group being updated. </p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group. The names must be unique to each billing group. </p>"""
    status: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_status.BillingGroupStatus"
    ]
    """<p>The status of the billing group. Only one of the valid values can be used. </p>"""
    computation_preference: NotRequired[
        "aws_sdk_billingconductor.types.computation_preference.ComputationPreference"
    ]
    """<p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_description.BillingGroupDescription"
    ]
    """<p>A description of the billing group. </p>"""
    account_grouping: NotRequired[
        "aws_sdk_billingconductor.types.update_billing_group_account_grouping.UpdateBillingGroupAccountGrouping"
    ]
    """<p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBillingGroupInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_billingconductor.types.billing_group_status

        out["Status"] = (
            aws_sdk_billingconductor.types.billing_group_status.serialize_json(
                value["status"]
            )
        )
    if "computation_preference" in value:
        import aws_sdk_billingconductor.types.computation_preference

        out["ComputationPreference"] = (
            aws_sdk_billingconductor.types.computation_preference.serialize_json(
                value["computation_preference"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "account_grouping" in value:
        import aws_sdk_billingconductor.types.update_billing_group_account_grouping

        out["AccountGrouping"] = (
            aws_sdk_billingconductor.types.update_billing_group_account_grouping.serialize_json(
                value["account_grouping"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBillingGroupInput:
    out: UpdateBillingGroupInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateBillingGroupInput.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_billingconductor.types.billing_group_status

        out["status"] = (
            aws_sdk_billingconductor.types.billing_group_status.deserialize_json(
                data["Status"]
            )
        )
    if "ComputationPreference" in data:
        import aws_sdk_billingconductor.types.computation_preference

        out["computation_preference"] = (
            aws_sdk_billingconductor.types.computation_preference.deserialize_json(
                data["ComputationPreference"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "AccountGrouping" in data:
        import aws_sdk_billingconductor.types.update_billing_group_account_grouping

        out["account_grouping"] = (
            aws_sdk_billingconductor.types.update_billing_group_account_grouping.deserialize_json(
                data["AccountGrouping"]
            )
        )
    return out
