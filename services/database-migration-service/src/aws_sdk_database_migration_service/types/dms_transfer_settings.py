"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DmsTransferSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DmsTransferSettings(TypedDict):
    service_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the <code>iam:PassRole</code> action.</p>"""
    bucket_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> The name of the S3 bucket to use. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DmsTransferSettings) -> dict:
    out: dict = {}
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DmsTransferSettings:
    out: DmsTransferSettings = {}  # type: ignore[typeddict-item]
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    return out
