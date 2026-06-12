"""Generated from Smithy shape ``com.amazonaws.billingconductor#AccountAssociationsListElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_email
    import aws_sdk_billingconductor.types.account_id
    import aws_sdk_billingconductor.types.account_name
    import aws_sdk_billingconductor.types.billing_group_arn


class AccountAssociationsListElement(TypedDict):
    account_id: NotRequired["aws_sdk_billingconductor.types.account_id.AccountId"]
    """<p>The associating array of account IDs.</p>"""
    billing_group_arn: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The Billing Group Arn that the linked account is associated to.</p>"""
    account_name: NotRequired["aws_sdk_billingconductor.types.account_name.AccountName"]
    """<p>The Amazon Web Services account name.</p>"""
    account_email: NotRequired[
        "aws_sdk_billingconductor.types.account_email.AccountEmail"
    ]
    """<p>The Amazon Web Services account email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAssociationsListElement) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "billing_group_arn" in value:
        out["BillingGroupArn"] = value["billing_group_arn"]
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "account_email" in value:
        out["AccountEmail"] = value["account_email"]
    return out


def deserialize_json(data: dict) -> AccountAssociationsListElement:
    out: AccountAssociationsListElement = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "BillingGroupArn" in data:
        out["billing_group_arn"] = data["BillingGroupArn"]
    if "AccountName" in data:
        out["account_name"] = data["AccountName"]
    if "AccountEmail" in data:
        out["account_email"] = data["AccountEmail"]
    return out
