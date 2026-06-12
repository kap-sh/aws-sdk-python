"""Generated from Smithy shape ``com.amazonaws.macie2#BucketPermissionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.account_level_permissions
    import aws_sdk_macie2.types.bucket_level_permissions


class BucketPermissionConfiguration(TypedDict):
    account_level_permissions: NotRequired[
        "aws_sdk_macie2.types.account_level_permissions.AccountLevelPermissions"
    ]
    """<p>The account-level permissions settings that apply to the bucket.</p>"""
    bucket_level_permissions: NotRequired[
        "aws_sdk_macie2.types.bucket_level_permissions.BucketLevelPermissions"
    ]
    """<p>The bucket-level permissions settings for the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketPermissionConfiguration) -> dict:
    out: dict = {}
    if "account_level_permissions" in value:
        import aws_sdk_macie2.types.account_level_permissions

        out["accountLevelPermissions"] = (
            aws_sdk_macie2.types.account_level_permissions.serialize_json(
                value["account_level_permissions"]
            )
        )
    if "bucket_level_permissions" in value:
        import aws_sdk_macie2.types.bucket_level_permissions

        out["bucketLevelPermissions"] = (
            aws_sdk_macie2.types.bucket_level_permissions.serialize_json(
                value["bucket_level_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BucketPermissionConfiguration:
    out: BucketPermissionConfiguration = {}  # type: ignore[typeddict-item]
    if "accountLevelPermissions" in data:
        import aws_sdk_macie2.types.account_level_permissions

        out["account_level_permissions"] = (
            aws_sdk_macie2.types.account_level_permissions.deserialize_json(
                data["accountLevelPermissions"]
            )
        )
    if "bucketLevelPermissions" in data:
        import aws_sdk_macie2.types.bucket_level_permissions

        out["bucket_level_permissions"] = (
            aws_sdk_macie2.types.bucket_level_permissions.deserialize_json(
                data["bucketLevelPermissions"]
            )
        )
    return out
