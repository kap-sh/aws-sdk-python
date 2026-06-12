"""Generated from Smithy shape ``com.amazonaws.guardduty#PermissionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_level_permissions
    import aws_sdk_guardduty.types.bucket_level_permissions


class PermissionConfiguration(TypedDict):
    bucket_level_permissions: NotRequired[
        "aws_sdk_guardduty.types.bucket_level_permissions.BucketLevelPermissions"
    ]
    """<p>Contains information about the bucket level permissions for the S3 bucket.</p>"""
    account_level_permissions: NotRequired[
        "aws_sdk_guardduty.types.account_level_permissions.AccountLevelPermissions"
    ]
    """<p>Contains information about the account level permissions on the S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionConfiguration) -> dict:
    out: dict = {}
    if "bucket_level_permissions" in value:
        import aws_sdk_guardduty.types.bucket_level_permissions

        out["bucketLevelPermissions"] = (
            aws_sdk_guardduty.types.bucket_level_permissions.serialize_json(
                value["bucket_level_permissions"]
            )
        )
    if "account_level_permissions" in value:
        import aws_sdk_guardduty.types.account_level_permissions

        out["accountLevelPermissions"] = (
            aws_sdk_guardduty.types.account_level_permissions.serialize_json(
                value["account_level_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionConfiguration:
    out: PermissionConfiguration = {}  # type: ignore[typeddict-item]
    if "bucketLevelPermissions" in data:
        import aws_sdk_guardduty.types.bucket_level_permissions

        out["bucket_level_permissions"] = (
            aws_sdk_guardduty.types.bucket_level_permissions.deserialize_json(
                data["bucketLevelPermissions"]
            )
        )
    if "accountLevelPermissions" in data:
        import aws_sdk_guardduty.types.account_level_permissions

        out["account_level_permissions"] = (
            aws_sdk_guardduty.types.account_level_permissions.deserialize_json(
                data["accountLevelPermissions"]
            )
        )
    return out
