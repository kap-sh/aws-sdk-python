"""Generated from Smithy shape ``com.amazonaws.appstream#AdminAppLicenseUsageRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.aws_account_id
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.timestamp


class AdminAppLicenseUsageRecord(TypedDict):
    user_arn: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The ARN of the user who used the license-included application.</p>"""
    billing_period: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The billing period for the license usage record.</p>"""
    owner_aws_account_id: NotRequired[
        "aws_sdk_appstream.types.aws_account_id.AwsAccountId"
    ]
    """<p>The account ID of the owner of the license.</p>"""
    subscription_first_used_date: NotRequired[
        "aws_sdk_appstream.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the license was first used.</p>"""
    subscription_last_used_date: NotRequired[
        "aws_sdk_appstream.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the license was last used.</p>"""
    license_type: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The type of license (for example, Microsoft Office).</p>"""
    user_id: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The ID of the user who used the license-included application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminAppLicenseUsageRecord) -> dict:
    out: dict = {}
    if "user_arn" in value:
        out["UserArn"] = value["user_arn"]
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "owner_aws_account_id" in value:
        out["OwnerAWSAccountId"] = value["owner_aws_account_id"]
    if "subscription_first_used_date" in value:
        import aws_sdk_appstream.types.timestamp

        out["SubscriptionFirstUsedDate"] = (
            aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
                value["subscription_first_used_date"]
            )
        )
    if "subscription_last_used_date" in value:
        import aws_sdk_appstream.types.timestamp

        out["SubscriptionLastUsedDate"] = (
            aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
                value["subscription_last_used_date"]
            )
        )
    if "license_type" in value:
        out["LicenseType"] = value["license_type"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminAppLicenseUsageRecord:
    out: AdminAppLicenseUsageRecord = {}  # type: ignore[typeddict-item]
    if "UserArn" in data:
        out["user_arn"] = data["UserArn"]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "OwnerAWSAccountId" in data:
        out["owner_aws_account_id"] = data["OwnerAWSAccountId"]
    if "SubscriptionFirstUsedDate" in data:
        import aws_sdk_appstream.types.timestamp

        out["subscription_first_used_date"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["SubscriptionFirstUsedDate"]
            )
        )
    if "SubscriptionLastUsedDate" in data:
        import aws_sdk_appstream.types.timestamp

        out["subscription_last_used_date"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["SubscriptionLastUsedDate"]
            )
        )
    if "LicenseType" in data:
        out["license_type"] = data["LicenseType"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    return out
