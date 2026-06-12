"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketVersioningConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3BucketBucketVersioningConfiguration(TypedDict):
    is_mfa_delete_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether MFA delete is currently enabled in the S3 bucket versioning configuration. If the S3 bucket was never configured with MFA delete, then this attribute is not included.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The versioning status of the S3 bucket. Valid values are <code>Enabled</code> or <code>Suspended</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketBucketVersioningConfiguration) -> dict:
    out: dict = {}
    if "is_mfa_delete_enabled" in value:
        out["IsMfaDeleteEnabled"] = value["is_mfa_delete_enabled"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketBucketVersioningConfiguration:
    out: AwsS3BucketBucketVersioningConfiguration = {}  # type: ignore[typeddict-item]
    if "IsMfaDeleteEnabled" in data:
        out["is_mfa_delete_enabled"] = data["IsMfaDeleteEnabled"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
