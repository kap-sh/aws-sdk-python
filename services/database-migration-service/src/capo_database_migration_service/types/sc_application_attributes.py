"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SCApplicationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class SCApplicationAttributes(TypedDict, closed=True):
    s3_bucket_path: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The path for the Amazon S3 bucket that the application uses for exporting assessment reports.</p>"""
    s3_bucket_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN for the role the application uses to access its Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SCApplicationAttributes) -> dict:
    out: dict = {}
    if "s3_bucket_path" in value:
        out["S3BucketPath"] = value["s3_bucket_path"]
    if "s3_bucket_role_arn" in value:
        out["S3BucketRoleArn"] = value["s3_bucket_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SCApplicationAttributes:
    out: SCApplicationAttributes = {}  # type: ignore[typeddict-item]
    if "S3BucketPath" in data:
        out["s3_bucket_path"] = data["S3BucketPath"]
    if "S3BucketRoleArn" in data:
        out["s3_bucket_role_arn"] = data["S3BucketRoleArn"]
    return out
