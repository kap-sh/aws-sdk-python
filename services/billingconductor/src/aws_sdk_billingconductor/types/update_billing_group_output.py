"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateBillingGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_id
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.billing_group_description
    import aws_sdk_billingconductor.types.billing_group_name
    import aws_sdk_billingconductor.types.billing_group_status
    import aws_sdk_billingconductor.types.billing_group_status_reason
    import aws_sdk_billingconductor.types.instant
    import aws_sdk_billingconductor.types.number_of_accounts
    import aws_sdk_billingconductor.types.pricing_plan_arn
    import aws_sdk_billingconductor.types.update_billing_group_account_grouping


class UpdateBillingGroupOutput(TypedDict):
    arn: NotRequired["aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the billing group that was updated. </p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_name.BillingGroupName"
    ]
    """<p> The name of the billing group. The names must be unique to each billing group. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_description.BillingGroupDescription"
    ]
    """<p> A description of the billing group. </p>"""
    primary_account_id: NotRequired[
        "aws_sdk_billingconductor.types.account_id.AccountId"
    ]
    """<p> The account ID that serves as the main account in a billing group. </p>"""
    pricing_plan_arn: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the pricing plan to compute Amazon Web Services charges for the billing group. </p>"""
    size: "aws_sdk_billingconductor.types.number_of_accounts.NumberOfAccounts"
    """<p> The number of accounts in the particular billing group. </p>"""
    last_modified_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p> The most recent time when the billing group was modified. </p>"""
    status: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_status.BillingGroupStatus"
    ]
    """<p> The status of the billing group. Only one of the valid values can be used. </p>"""
    status_reason: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_status_reason.BillingGroupStatusReason"
    ]
    """<p> The reason why the billing group is in its current status. </p>"""
    account_grouping: NotRequired[
        "aws_sdk_billingconductor.types.update_billing_group_account_grouping.UpdateBillingGroupAccountGrouping"
    ]
    """<p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBillingGroupOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "primary_account_id" in value:
        out["PrimaryAccountId"] = value["primary_account_id"]
    if "pricing_plan_arn" in value:
        out["PricingPlanArn"] = value["pricing_plan_arn"]
    out["Size"] = value.get("size", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    if "status" in value:
        import aws_sdk_billingconductor.types.billing_group_status

        out["Status"] = (
            aws_sdk_billingconductor.types.billing_group_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "account_grouping" in value:
        import aws_sdk_billingconductor.types.update_billing_group_account_grouping

        out["AccountGrouping"] = (
            aws_sdk_billingconductor.types.update_billing_group_account_grouping.serialize_json(
                value["account_grouping"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBillingGroupOutput:
    out: UpdateBillingGroupOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "PrimaryAccountId" in data:
        out["primary_account_id"] = data["PrimaryAccountId"]
    if "PricingPlanArn" in data:
        out["pricing_plan_arn"] = data["PricingPlanArn"]
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if "LastModifiedTime" in data:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if "Status" in data:
        import aws_sdk_billingconductor.types.billing_group_status

        out["status"] = (
            aws_sdk_billingconductor.types.billing_group_status.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "AccountGrouping" in data:
        import aws_sdk_billingconductor.types.update_billing_group_account_grouping

        out["account_grouping"] = (
            aws_sdk_billingconductor.types.update_billing_group_account_grouping.deserialize_json(
                data["AccountGrouping"]
            )
        )
    return out
