"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupListElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_id
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.billing_group_description
    import aws_sdk_billingconductor.types.billing_group_name
    import aws_sdk_billingconductor.types.billing_group_status
    import aws_sdk_billingconductor.types.billing_group_status_reason
    import aws_sdk_billingconductor.types.billing_group_type
    import aws_sdk_billingconductor.types.computation_preference
    import aws_sdk_billingconductor.types.instant
    import aws_sdk_billingconductor.types.list_billing_group_account_grouping
    import aws_sdk_billingconductor.types.number_of_accounts


class BillingGroupListElement(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group.</p>"""
    arn: NotRequired["aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"]
    """<p>The Amazon Resource Number (ARN) that can be used to uniquely identify the billing group.</p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_description.BillingGroupDescription"
    ]
    """<p>The description of the billing group.</p>"""
    primary_account_id: NotRequired[
        "aws_sdk_billingconductor.types.account_id.AccountId"
    ]
    """<p>The account ID that serves as the main account in a billing group.</p>"""
    computation_preference: NotRequired[
        "aws_sdk_billingconductor.types.computation_preference.ComputationPreference"
    ]
    size: "aws_sdk_billingconductor.types.number_of_accounts.NumberOfAccounts"
    """<p>The number of accounts in the particular billing group.</p>"""
    creation_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p>The time when the billing group was created.</p>"""
    last_modified_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p>The most recent time when the billing group was modified.</p>"""
    status: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_status.BillingGroupStatus"
    ]
    """<p>The billing group status. Only one of the valid values can be used.</p>"""
    status_reason: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_status_reason.BillingGroupStatusReason"
    ]
    """<p>The reason why the billing group is in its current status.</p>"""
    account_grouping: NotRequired[
        "aws_sdk_billingconductor.types.list_billing_group_account_grouping.ListBillingGroupAccountGrouping"
    ]
    """<p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>"""
    billing_group_type: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_type.BillingGroupType"
    ]
    """<p> The type of billing group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupListElement) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "primary_account_id" in value:
        out["PrimaryAccountId"] = value["primary_account_id"]
    if "computation_preference" in value:
        import aws_sdk_billingconductor.types.computation_preference

        out["ComputationPreference"] = (
            aws_sdk_billingconductor.types.computation_preference.serialize_json(
                value["computation_preference"]
            )
        )
    out["Size"] = value.get("size", 0)
    out["CreationTime"] = value.get("creation_time", 0)
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
        import aws_sdk_billingconductor.types.list_billing_group_account_grouping

        out["AccountGrouping"] = (
            aws_sdk_billingconductor.types.list_billing_group_account_grouping.serialize_json(
                value["account_grouping"]
            )
        )
    if "billing_group_type" in value:
        import aws_sdk_billingconductor.types.billing_group_type

        out["BillingGroupType"] = (
            aws_sdk_billingconductor.types.billing_group_type.serialize_json(
                value["billing_group_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> BillingGroupListElement:
    out: BillingGroupListElement = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "PrimaryAccountId" in data:
        out["primary_account_id"] = data["PrimaryAccountId"]
    if "ComputationPreference" in data:
        import aws_sdk_billingconductor.types.computation_preference

        out["computation_preference"] = (
            aws_sdk_billingconductor.types.computation_preference.deserialize_json(
                data["ComputationPreference"]
            )
        )
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    else:
        out["creation_time"] = 0
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
        import aws_sdk_billingconductor.types.list_billing_group_account_grouping

        out["account_grouping"] = (
            aws_sdk_billingconductor.types.list_billing_group_account_grouping.deserialize_json(
                data["AccountGrouping"]
            )
        )
    if "BillingGroupType" in data:
        import aws_sdk_billingconductor.types.billing_group_type

        out["billing_group_type"] = (
            aws_sdk_billingconductor.types.billing_group_type.deserialize_json(
                data["BillingGroupType"]
            )
        )
    return out
