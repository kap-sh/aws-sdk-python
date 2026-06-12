"""Generated from Smithy shape ``com.amazonaws.datasync#S3ManifestConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.iam_role_arn
    import aws_sdk_datasync.types.s3_bucket_arn
    import aws_sdk_datasync.types.s3_object_version_id
    import aws_sdk_datasync.types.s3_subdirectory


class S3ManifestConfig(TypedDict):
    manifest_object_path: "aws_sdk_datasync.types.s3_subdirectory.S3Subdirectory"
    """<p>Specifies the Amazon S3 object key of your manifest. This can include a prefix (for example, <code>prefix/my-manifest.csv</code>).</p>"""
    bucket_access_role_arn: "aws_sdk_datasync.types.iam_role_arn.IamRoleArn"
    """<p>Specifies the Identity and Access Management (IAM) role that allows DataSync to access your manifest. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access\">Providing DataSync access to your manifest</a>.</p>"""
    s3_bucket_arn: "aws_sdk_datasync.types.s3_bucket_arn.S3BucketArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the S3 bucket where you're hosting your manifest.</p>"""
    manifest_object_version_id: NotRequired[
        "aws_sdk_datasync.types.s3_object_version_id.S3ObjectVersionId"
    ]
    """<p>Specifies the object version ID of the manifest that you want DataSync to use. If you don't set this, DataSync uses the latest version of the object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ManifestConfig) -> dict:
    out: dict = {}
    out["ManifestObjectPath"] = value["manifest_object_path"]
    out["BucketAccessRoleArn"] = value["bucket_access_role_arn"]
    out["S3BucketArn"] = value["s3_bucket_arn"]
    if "manifest_object_version_id" in value:
        out["ManifestObjectVersionId"] = value["manifest_object_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ManifestConfig:
    out: S3ManifestConfig = {}  # type: ignore[typeddict-item]
    if "ManifestObjectPath" in data:
        out["manifest_object_path"] = data["ManifestObjectPath"]
    else:
        raise DeserializationError("S3ManifestConfig.manifest_object_path required")
    if "BucketAccessRoleArn" in data:
        out["bucket_access_role_arn"] = data["BucketAccessRoleArn"]
    else:
        raise DeserializationError("S3ManifestConfig.bucket_access_role_arn required")
    if "S3BucketArn" in data:
        out["s3_bucket_arn"] = data["S3BucketArn"]
    else:
        raise DeserializationError("S3ManifestConfig.s3_bucket_arn required")
    if "ManifestObjectVersionId" in data:
        out["manifest_object_version_id"] = data["ManifestObjectVersionId"]
    return out
