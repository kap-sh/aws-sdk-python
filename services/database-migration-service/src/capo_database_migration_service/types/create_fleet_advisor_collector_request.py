"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateFleetAdvisorCollectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class CreateFleetAdvisorCollectorRequest(TypedDict, closed=True):
    collector_name: "capo_database_migration_service.types.string.String"
    """<p>The name of your Fleet Advisor collector (for example, <code>sample-collector</code>).</p>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A summary description of your Fleet Advisor collector.</p>"""
    service_access_role_arn: "capo_database_migration_service.types.string.String"
    """<p>The IAM role that grants permissions to access the specified Amazon S3 bucket.</p>"""
    s3_bucket_name: "capo_database_migration_service.types.string.String"
    """<p>The Amazon S3 bucket that the Fleet Advisor collector uses to store inventory metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFleetAdvisorCollectorRequest) -> dict:
    out: dict = {}
    out["CollectorName"] = value["collector_name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    out["S3BucketName"] = value["s3_bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFleetAdvisorCollectorRequest:
    out: CreateFleetAdvisorCollectorRequest = {}  # type: ignore[typeddict-item]
    if "CollectorName" in data:
        out["collector_name"] = data["CollectorName"]
    else:
        raise DeserializationError(
            "CreateFleetAdvisorCollectorRequest.collector_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    else:
        raise DeserializationError(
            "CreateFleetAdvisorCollectorRequest.service_access_role_arn required"
        )
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        raise DeserializationError(
            "CreateFleetAdvisorCollectorRequest.s3_bucket_name required"
        )
    return out
