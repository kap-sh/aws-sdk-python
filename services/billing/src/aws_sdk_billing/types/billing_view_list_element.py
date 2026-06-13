"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewListElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billing.types.account_id
    import aws_sdk_billing.types.billing_view_arn
    import aws_sdk_billing.types.billing_view_description
    import aws_sdk_billing.types.billing_view_health_status
    import aws_sdk_billing.types.billing_view_name
    import aws_sdk_billing.types.billing_view_type


class BillingViewListElement(TypedDict):
    arn: NotRequired["aws_sdk_billing.types.billing_view_arn.BillingViewArn"]
    """<p>The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    name: NotRequired["aws_sdk_billing.types.billing_view_name.BillingViewName"]
    """<p> A list of names of the Billing view. </p>"""
    description: NotRequired[
        "aws_sdk_billing.types.billing_view_description.BillingViewDescription"
    ]
    """<p> The description of the billing view. </p>"""
    owner_account_id: NotRequired["aws_sdk_billing.types.account_id.AccountId"]
    """<p> The list of owners of the Billing view. </p>"""
    source_account_id: NotRequired["aws_sdk_billing.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID that owns the source billing view, if this is a derived billing view. </p>"""
    billing_view_type: NotRequired[
        "aws_sdk_billing.types.billing_view_type.BillingViewType"
    ]
    """<p>The type of billing view.</p>"""
    health_status: NotRequired[
        "aws_sdk_billing.types.billing_view_health_status.BillingViewHealthStatus"
    ]
    """<p> The current health status of the billing view. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewListElement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "owner_account_id" in value:
        out["ownerAccountId"] = value["owner_account_id"]
    if "source_account_id" in value:
        out["sourceAccountId"] = value["source_account_id"]
    if "billing_view_type" in value:
        import aws_sdk_billing.types.billing_view_type

        out["billingViewType"] = (
            aws_sdk_billing.types.billing_view_type.serialize_aws_json_1_0(
                value["billing_view_type"]
            )
        )
    if "health_status" in value:
        import aws_sdk_billing.types.billing_view_health_status

        out["healthStatus"] = (
            aws_sdk_billing.types.billing_view_health_status.serialize_aws_json_1_0(
                value["health_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingViewListElement:
    out: BillingViewListElement = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "ownerAccountId" in data:
        out["owner_account_id"] = data["ownerAccountId"]
    if "sourceAccountId" in data:
        out["source_account_id"] = data["sourceAccountId"]
    if "billingViewType" in data:
        import aws_sdk_billing.types.billing_view_type

        out["billing_view_type"] = (
            aws_sdk_billing.types.billing_view_type.deserialize_aws_json_1_0(
                data["billingViewType"]
            )
        )
    if "healthStatus" in data:
        import aws_sdk_billing.types.billing_view_health_status

        out["health_status"] = (
            aws_sdk_billing.types.billing_view_health_status.deserialize_aws_json_1_0(
                data["healthStatus"]
            )
        )
    return out
