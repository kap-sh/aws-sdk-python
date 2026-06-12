"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateFleetAdvisorCollectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class CreateFleetAdvisorCollectorResponse(TypedDict):
    collector_referenced_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The unique ID of the new Fleet Advisor collector, for example: <code>22fda70c-40d5-4acf-b233-a495bd8eb7f5</code> </p>"""
    collector_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name of the new Fleet Advisor collector.</p>"""
    description: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A summary description of the Fleet Advisor collector.</p>"""
    service_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The IAM role that grants permissions to access the specified Amazon S3 bucket.</p>"""
    s3_bucket_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon S3 bucket that the collector uses to store inventory metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetAdvisorCollectorResponse) -> dict:
    out: dict = {}
    if "collector_referenced_id" in value:
        out["CollectorReferencedId"] = value["collector_referenced_id"]
    if "collector_name" in value:
        out["CollectorName"] = value["collector_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetAdvisorCollectorResponse:
    out: CreateFleetAdvisorCollectorResponse = {}  # type: ignore[typeddict-item]
    if "CollectorReferencedId" in data:
        out["collector_referenced_id"] = data["CollectorReferencedId"]
    if "CollectorName" in data:
        out["collector_name"] = data["CollectorName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    return out
